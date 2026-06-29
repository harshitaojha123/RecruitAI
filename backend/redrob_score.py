def redrob_score(candidate):

    s = candidate["redrob_signals"]

    score = 0

    score += s["profile_completeness_score"] * 0.10

    # Reduced popularity bias
    score += s["saved_by_recruiters_30d"] * 0.5

    score += s["search_appearance_30d"] * 0.05

    score += s["endorsements_received"] * 0.05

    score += s["connection_count"] * 0.01

    score += s["interview_completion_rate"] * 15

    score += s["recruiter_response_rate"] * 15

    offer_rate = s["offer_acceptance_rate"]

    if offer_rate != -1:
        score += offer_rate * 10

    if s["verified_email"]:
        score += 3

    if s["verified_phone"]:
        score += 3

    if s["linkedin_connected"]:
        score += 3

    return score