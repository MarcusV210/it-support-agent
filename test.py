from qdrant_client import QdrantClient
Q_client = QdrantClient(url='http://localhost:6333')
Q_client.delete_collection("it_support")