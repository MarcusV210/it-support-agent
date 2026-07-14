# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient, models
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer
# pyrefly: ignore [missing-import]
from flashrank import Ranker, RerankRequest



def hybrid_search(model_name = "google/embeddinggemma-300m", query = "What is an error?", limit = 10):


    model = SentenceTransformer(model_name)

    Q_client = QdrantClient(url='http://localhost:6333')
    COLLECTION_NAME = "it_support"

    embedded_query = model.encode(query, normalize_embeddings=True, show_progress_bar=True).tolist()

    dense_results = Q_client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedded_query,
        using="dense",
        limit=10
    )

    bm25_results = Q_client.query_points(
        collection_name=COLLECTION_NAME,
        query=models.Document(text=query, model="Qdrant/bm25"),
        using="bm25",
        limit=10
    )

    # Deduplicate by point id
    seen = set()
    all_results = []
    for point in dense_results.points + bm25_results.points:
        if point.id not in seen:
            seen.add(point.id)
            all_results.append(point)

    # Rerank with FlashRank
    ranker = Ranker()
    rerank_request = RerankRequest(
        query=query,
        passages=[{"id": p.id, "text": p.payload["content"]} for p in all_results]
    )
    reranked = ranker.rerank(rerank_request)[:10]

    return reranked