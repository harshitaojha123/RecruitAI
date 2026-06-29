def history_score(candidate, jd_text):

    jd_keywords = [
        word.lower()
        for word in jd_text.split()
        if len(word) > 3
    ]

    score = 0

    for job in candidate["career_history"]:

        text = job["description"].lower()

        for keyword in jd_keywords:

            if keyword in text:
                score += 2

    return score