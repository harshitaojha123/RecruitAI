from jd_skills import JD_SKILLS


def calculate_score(candidate):

    score = 0

    candidate_skills = [
        skill["name"]
        for skill in candidate["skills"]
    ]

    # Skill match
    matches = 0

    for skill in JD_SKILLS:
        if skill in candidate_skills:
            matches += 1

    score += matches * 5

    # Experience
    years = candidate["profile"]["years_of_experience"]

    if years >= 5:
        score += 20

    # Open to work
    if candidate["redrob_signals"]["open_to_work_flag"]:
        score += 10

    # Recruiter signals
    signals = candidate["redrob_signals"]

    score += signals["github_activity_score"]

    score += signals["recruiter_response_rate"] * 20

    score += signals["interview_completion_rate"] * 20

    return round(score, 2)