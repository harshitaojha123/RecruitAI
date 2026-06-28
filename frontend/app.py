import streamlit as st
import sys
import os

# Add backend folder to Python path
sys.path.append(
    os.path.abspath("../backend")
)

from rank_candidates import rank_candidates

st.set_page_config(
    page_title="RecruitAI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RecruitAI")

st.subheader(
    "AI-Powered Candidate Discovery & Ranking System"
)

jd_text = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button(
    "Rank Candidates",
    type="primary"
):

    if not jd_text.strip():

        st.warning(
            "Please paste a Job Description first."
        )

    else:

        st.info(
            "Ranking candidates..."
        )

        results = rank_candidates(
            jd_text
        )

        st.success(
            "Ranking Completed!"
        )

        st.subheader(
            "🏆 Top Candidates"
        )

        # Dashboard metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Candidates Returned",
                len(results)
            )

        with col2:
            st.metric(
                "Top Score",
                results[0]["score"]
            )

        with col3:
            st.metric(
                "Best Match",
                results[0]["candidate_id"]
            )

        st.divider()

        for rank, candidate in enumerate(
            results,
            start=1
        ):

            with st.container(
                border=True
            ):

                st.markdown(
                    f"## 🏅 Rank #{rank}"
                )

                col1, col2 = st.columns(
                    [2, 1]
                )

                with col1:

                    st.write(
                        f"**Candidate ID:** {candidate['candidate_id']}"
                    )

                    st.write(
                        f"**Title:** {candidate['title']}"
                    )

                    st.write(
                        f"**Experience:** {candidate['experience']} years"
                    )

                with col2:

                    st.metric(
                        "Match Score",
                        candidate["score"]
                    )

                st.markdown(
                    "### Skills"
                )

                st.info(
                    " | ".join(
                        candidate["skills"][:10]
                    )
                )

                st.markdown(
                    "### Professional Summary"
                )

                st.write(
                    candidate["summary"]
                )

                st.markdown(
                    "### Why Recommended"
                )

                for reason in candidate["reasons"]:

                    st.success(
                        f"✓ {reason}"
                    )

                st.divider()