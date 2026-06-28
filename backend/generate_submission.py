import pandas as pd

from rank_candidates import rank_candidates

JD = """
Senior AI Engineer

Need experience in:
Python
LLMs
NLP
Embeddings
Vector Databases
RAG
"""

results = rank_candidates(JD)

rows = []

for rank, candidate in enumerate(
    results,
    start=1
):

    rows.append(
        {
            "candidate_id":
                candidate["candidate_id"],
            "rank":
                rank,
            "score":
                candidate["score"]
        }
    )

df = pd.DataFrame(rows)

df.to_csv(
    "submission.csv",
    index=False
)

print("submission.csv created")