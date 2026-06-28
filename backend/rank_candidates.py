import os
import json

from batch_ranker import MODEL
from sklearn.metrics.pairwise import cosine_similarity


def rank_candidates(jd_text):

    data_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "raw",
        "candidates.jsonl"
    )

    jd_embedding = MODEL.encode(
        [jd_text],
        normalize_embeddings=True
    )

    results = []

    with open(
        data_file,
        "r",
        encoding="utf-8"
    ) as f:

        for i, line in enumerate(f):

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
                candidate["profile"]["summary"]
                + " "
                + career_text
                + " "
                + skills_text
            )

            candidate_embedding = MODEL.encode(
                [text],
                normalize_embeddings=True
            )

            semantic_score = cosine_similarity(
                candidate_embedding,
                jd_embedding
            )[0][0]

            years = candidate["profile"][
                "years_of_experience"
            ]

            signals = candidate[
                "redrob_signals"
            ]

            final_score = semantic_score * 70

            final_score += (
                min(years, 10) * 2
            )

            final_score += signals[
                "github_activity_score"
            ]

            final_score += (
                signals[
                    "recruiter_response_rate"
                ] * 5
            )

            final_score += (
                signals[
                    "interview_completion_rate"
                ] * 5
            )

            if signals[
                "open_to_work_flag"
            ]:
                final_score += 5

            reasons = []

            if semantic_score >= 0.60:
                reasons.append(
                    "Strong semantic match"
                )

            if years >= 5:
                reasons.append(
                    "Experienced candidate"
                )

            if signals[
                "github_activity_score"
            ] >= 7:
                reasons.append(
                    "High GitHub activity"
                )

            if signals[
                "open_to_work_flag"
            ]:
                reasons.append(
                    "Open to work"
                )

            results.append(
                {
                    "candidate_id":
                        candidate["candidate_id"],

                    "title":
                        candidate["profile"][
                            "current_title"
                        ],

                    "experience":
                        years,

                    "summary":
                        candidate["profile"][
                            "summary"
                        ],

                    "skills":
                        [
                            skill["name"]
                            for skill in candidate[
                                "skills"
                            ]
                        ],

                    "score":
                        round(
                            final_score,
                            2
                        ),

                    "reasons":
                        reasons
                }
            )

            # Testing on first 500
            if i >= 500:
                break

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:10]