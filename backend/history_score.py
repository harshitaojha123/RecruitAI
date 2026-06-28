KEYWORDS = [
    "retrieval",
    "ranking",
    "recommendation",
    "embedding",
    "vector",
    "search",
    "machine learning",
    "ml",
    "ai",
    "nlp",
    "production",
    "ab testing",
    "evaluation"
]


def history_score(candidate):

    score = 0

    for job in candidate["career_history"]:

        text = job["description"].lower()

        for keyword in KEYWORDS:

            if keyword in text:
                score += 5

    return score