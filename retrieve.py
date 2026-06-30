# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("google/embeddinggemma-300m")

Q_client = QdrantClient(url='http://localhost:6333')
COLLECTION_NAME = "it_support"

dummy_query = input()

embedded_query = model.encode(dummy_query, normalize_embeddings=True, show_progress_bar=True).tolist()

results = Q_client.query_points(
    collection_name=COLLECTION_NAME,
    prefetch=[
        models.Prefetch(
            query=embedded_query,
            using="dense",
            limit=10
        ),
        models.Prefetch(
            query=models.Document(text=dummy_query, model="Qdrant/bm25"),
            using="bm25",
            limit=10
        )
    ],
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    limit=10
)


for i, result in enumerate(results.points, start=1):

    print("="*80)

    print(f"Result {i}")

    print(f"Score : {result.score:.4f}")

    print(result.payload["content"])