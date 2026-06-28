from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

JD_TEXT = """
Senior AI Engineer.
Embeddings, retrieval, ranking,
vector databases, NLP,
production ML systems,
evaluation frameworks.
"""

JD_EMBEDDING = model.encode(
    JD_TEXT,
    normalize_embeddings=True
)