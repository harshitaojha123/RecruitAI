import json
from batch_ranker import MODEL, JD_EMBEDDING
from sklearn.metrics.pairwise import cosine_similarity

BATCH_SIZE = 1000

results = []

texts = []
candidate_ids = []

processed = 0

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(line)

        text = (
            candidate["profile"]["summary"]
            + " "
            + " ".join(
                skill["name"]
                for skill in candidate["skills"]
            )
        )

        texts.append(text)
        candidate_ids.append(
            candidate["candidate_id"]
        )

        if len(texts) == BATCH_SIZE:

            embeddings = MODEL.encode(
                texts,
                normalize_embeddings=True,
                show_progress_bar=False
            )

            scores = cosine_similarity(
                embeddings,
                JD_EMBEDDING
            )

            for cid, score in zip(
                candidate_ids,
                scores
            ):
                results.append(
                    (
                        cid,
                        float(score[0])
                    )
                )

            processed += len(texts)

            print(
                "Processed:",
                processed
            )

            texts = []
            candidate_ids = []

results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTOP 10\n")

for cid, score in results[:10]:

    print(
        cid,
        round(score, 4)
    )