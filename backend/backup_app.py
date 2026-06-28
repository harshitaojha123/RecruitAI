import json

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    first_candidate = json.loads(
        next(f)
    )

print(first_candidate.keys())

print(
    "\nCandidate ID:",
    first_candidate["candidate_id"]
)