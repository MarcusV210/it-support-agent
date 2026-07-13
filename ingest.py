import uuid
from pathlib import Path
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer
# pyrefly: ignore [missing-import]
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient, models

# Embeddings models
dense_model = SentenceTransformer("google/embeddinggemma-300m", device='cpu')

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def add_chunk_metadata(chunk_content, document, chunk_id=None, page=None, **kwargs):

    metadata = {
        "chunk_id": chunk_id or str(uuid.uuid4()),
        "document": str(document),
        "page": page,
    }
    metadata.update(kwargs)
    return {
        "content": chunk_content,
        "metadata": metadata
    }


def split_markdown(path):

    # Splits on headers to preserve structure
    md = path.read_text(encoding="utf-8")

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "h1"),
            ("##", "h2"),
            ("###", "h3")
        ]
    )
    header_docs = header_splitter.split_text(md)

    # Splits the header chunks further
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for i, doc in enumerate(header_docs):
        split_chunks = text_splitter.split_text(doc.page_content)
        for j, text in enumerate(split_chunks):
            chunk_id = f"{path.stem}_{i}_{j}"
            chunk_with_meta = add_chunk_metadata(
                chunk_content=text,
                document=path.name,
                chunk_id=chunk_id,
                headers=doc.metadata
            )
            chunks.append(chunk_with_meta)

    return chunks

chunks = []

for md_file in Path("./docs/md_input").glob("*.md"):
    chunks.extend(split_markdown(md_file))

print(f"1. Chunking completed. Length : {len(chunks)}")



# Extract just the text content for embedding
chunk_texts = [c["content"] for c in chunks]

dense_vectors = dense_model.encode(
    chunk_texts,
    batch_size=128,
    normalize_embeddings=True, # Good for cosine similarity
    show_progress_bar=True
)

print(f"2. \nChunks: {len(chunks)}")
print(f"Dense : {len(dense_vectors)}")



# Qdrant setup

Q_client = QdrantClient(url='http://localhost:6333')
collections = Q_client.get_collections().collections
existing_collections = [c.name for c in collections]

COLLECTION_NAME = "it_support"
EMBEDDING_DIM = dense_model.get_embedding_dimension()

if COLLECTION_NAME not in existing_collections:

    Q_client.create_collection(
        COLLECTION_NAME,
        vectors_config={"dense": models.VectorParams(size=EMBEDDING_DIM, distance=models.Distance.COSINE)},
        sparse_vectors_config={
            "bm25": models.SparseVectorParams(modifier=models.Modifier.IDF)
        }
    )

    print(f"3. Collection {COLLECTION_NAME} created. ")
else:
    print(f"3. Collection {COLLECTION_NAME} already exists")


# Populate points
# Note: sparse vector is NOT precomputed here. We pass models.Document(text=...)
# and Qdrant's server-side FastEmbed integration converts it into a BM25 sparse
# vector (term indices + weights) automatically during upsert.
points = []

for i, (chunk, dense_vector) in enumerate(zip(chunks, dense_vectors)):

    points.append(
        models.PointStruct(
            id=i,
            vector={
                "dense": dense_vector.tolist(),
                "bm25": models.Document(
                    text=chunk["content"],
                    model="Qdrant/bm25"
                )
            },
            payload={
                "content": chunk["content"],
                "text": chunk['content'],
                **chunk["metadata"]
            }
        )
    )


# Upserting to QDrant in batches
def batch_upsert_to_qdrant(points, batch_size=100):

    for batch_num, i in enumerate(range(0, len(points), batch_size), start=1):
        batch = points[i:i + batch_size]

        print(f"Batch {batch_num} | Uploaded {min(i + batch_size, len(points))}/{len(points)}")

        try:
            Q_client.upsert(
                collection_name=COLLECTION_NAME,
                points=batch # Putting batch_size at a time.
            )
        except Exception as e:
            print(f"Batch {batch_num} failed. Error : {e}")



batch_upsert_to_qdrant(points=points, batch_size=100)

print(f"4. Uploaded to QDrant under {COLLECTION_NAME}")