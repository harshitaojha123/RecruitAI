import os
import json
import numpy as np

from batch_ranker import MODEL

data_file = os.path.join(
    os.path.dirname(__file__),
    "data",
    "raw",
    "candidates.jsonl"
)

texts = []

with open(data_file, "r", encoding="utf-8") as f:

    for i, line in enumerate(f):

        if i % 5000 == 0:
            print(f"Loaded {i} candidates")

        candidate = json.loads(line)

        career_text = " ".join(
            job["description"]
            for job in candidate["career_history"]
        )

        skills_text = " ".join(
            skill["name"]
            for skill in candidate["skills"]
        )

        text = (
            candidate["profile"]["headline"]
            + " "
            + candidate["profile"]["current_title"]
            + " "
            + candidate["profile"]["summary"]
            + " "
            + career_text
            + " "
            + skills_text
        )

        texts.append(text)

print("Generating embeddings...")

embeddings = MODEL.encode(
    texts,
    batch_size=256,
    normalize_embeddings=True,
    show_progress_bar=True
)

np.save(
    "candidate_embeddings.npy",
    embeddings
)

print("Embeddings saved.")