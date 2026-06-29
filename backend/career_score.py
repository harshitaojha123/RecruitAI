def career_score(candidate, jd_text):

    score = 0

    title = candidate["profile"][
        "current_title"
    ].lower()

    jd = jd_text.lower()

    # AI / ML roles
    if any(
        word in jd
        for word in [
            "ai",
            "machine learning",
            "ml",
            "nlp",
            "llm",
            "rag",
            "data scientist"
        ]
    ):

        ai_titles = [
            "machine learning engineer",
            "ml engineer",
            "ai engineer",
            "applied scientist",
            "recommendation systems engineer",
            "search engineer",
            "nlp engineer",
            "data scientist"
        ]

        if any(
            t in title
            for t in ai_titles
        ):
            score += 30
        else:
            score -= 20

    # HR roles
    elif any(
        word in jd
        for word in [
            "hr",
            "human resources",
            "talent acquisition",
            "recruitment",
            "recruiter"
        ]
    ):

        hr_titles = [
            "hr manager",
            "recruiter",
            "talent acquisition",
            "human resources"
        ]

        if any(
            t in title
            for t in hr_titles
        ):
            score += 30
        else:
            score -= 20

    return score


def availability_score(candidate):

    score = 0

    signals = candidate["redrob_signals"]

    if signals["open_to_work_flag"]:
        score += 15

    notice = signals["notice_period_days"]

    if notice <= 30:
        score += 15
    elif notice <= 60:
        score += 5
    else:
        score -= 10

    return score