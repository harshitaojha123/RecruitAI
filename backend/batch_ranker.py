import json
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

JD_TEXT = """
Senior AI Engineer.

Need production experience with:
embeddings,
retrieval systems,
ranking systems,
vector databases,
evaluation frameworks,
Python,
NLP,
LLMs,
fine tuning,
hybrid search,
A/B testing.

Must have shipped production AI systems.
"""

JD_EMBEDDING = MODEL.encode(
    [JD_TEXT],
    normalize_embeddings=True
)