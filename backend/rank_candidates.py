import os
import json
import numpy as np

from batch_ranker import MODEL
from sklearn.metrics.pairwise import cosine_similarity

from career_score import career_score, availability_score
from history_score import history_score
from redrob_score import redrob_score


def rank_candidates(jd_text):

    data_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "raw",
        "candidates.jsonl"
    )

    embeddings_file = os.path.join(
        os.path.dirname(__file__),
        "candidate_embeddings.npy"
    )

    print("Loading candidate embeddings...")

    candidate_embeddings = np.load(
        embeddings_file
    )

    print(
        f"Loaded {len(candidate_embeddings)} embeddings"
    )

    print("Encoding job description...")

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

            if i >= len(candidate_embeddings):
                break

            candidate = json.loads(line)

            semantic_score = cosine_similarity(
                candidate_embeddings[i].reshape(1, -1),
                jd_embedding
            )[0][0]

            years = candidate["profile"][
                "years_of_experience"
            ]

            signals = candidate[
                "redrob_signals"
            ]

            github_score = max(
                signals["github_activity_score"],
                0
            )

            final_score = semantic_score * 50

            final_score += (
                min(years, 10) * 2
            )

            final_score += career_score(
                candidate,
                jd_text
            )

            final_score += history_score(
                candidate
            )

            final_score += availability_score(
                candidate
            )

            final_score += redrob_score(
                candidate
            )

            final_score += (
                github_score * 0.20
            )

            reasons = []

            if semantic_score >= 0.60:
                reasons.append(
                    "Strong semantic alignment with role"
                )

            if years >= 5:
                reasons.append(
                    f"{years} years of experience"
                )

            if github_score >= 50:
                reasons.append(
                    "Active GitHub contributor"
                )

            if signals["open_to_work_flag"]:
                reasons.append(
                    "Open to work"
                )

            if (
                signals["saved_by_recruiters_30d"]
                > 5
            ):
                reasons.append(
                    "Frequently saved by recruiters"
                )

            if (
                signals["profile_completeness_score"]
                >= 90
            ):
                reasons.append(
                    "Highly complete profile"
                )

            if (
                signals["interview_completion_rate"]
                >= 0.80
            ):
                reasons.append(
                    "Strong interview attendance"
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

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:10]