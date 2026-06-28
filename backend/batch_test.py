import json

texts = []

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for i, line in enumerate(f):

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

        if i == 999:
            break

print(
    "Candidates loaded:",
    len(texts)
)

print(
    "First text length:",
    len(texts[0])
)