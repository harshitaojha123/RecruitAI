AI_TITLES = [
    "Machine Learning Engineer",
    "ML Engineer",
    "AI Engineer",
    "Applied Scientist",
    "Recommendation Systems Engineer",
    "Search Engineer",
    "NLP Engineer",
    "Data Scientist"
]

BAD_TITLES = [
    "HR Manager",
    "Marketing Manager",
    "Project Manager",
    "Sales Executive",
    "Customer Support"
]


def career_score(candidate):

    score = 0

    title = candidate["profile"]["current_title"]

    for good_title in AI_TITLES:

        if good_title.lower() in title.lower():
            score += 30

    for bad_title in BAD_TITLES:

        if bad_title.lower() in title.lower():
            score -= 40


            

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