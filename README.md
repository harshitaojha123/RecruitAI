<div align="center">

# 🤖 RecruitAI

### AI-Powered Candidate Discovery & Ranking System

🚀 Understanding Job Descriptions Beyond Keywords

[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)]
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)]
[![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)]
[![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-NLP-orange?style=for-the-badge)]

</div>

---

## 🎯 Problem Statement

Recruiters often review hundreds of profiles and still miss top talent because traditional Applicant Tracking Systems rely heavily on keyword matching.

RecruitAI solves this problem by:

✅ Understanding Job Descriptions semantically

✅ Evaluating complete candidate profiles

✅ Leveraging recruiter signals and career history

✅ Generating explainable candidate rankings

✅ Producing recruiter-ready shortlists

---

## ✨ Key Features

| Feature | Description |
|----------|------------|
| 🧠 Semantic Matching | Understands candidate relevance using embeddings |
| 📊 Hybrid Ranking | Combines AI similarity + recruiter signals |
| 🎯 Candidate Discovery | Finds strong candidates beyond keyword matching |
| 📈 Explainable AI | Shows why candidates were recommended |
| ⚡ Streamlit Dashboard | Interactive recruiter interface |
| 📄 Submission Generation | Generates ranked candidate output CSV |

---

## 🏗️ System Architecture

```text
```text
                         ┌─────────────────────┐
                         │  Job Description    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                     ┌─────────────────────────┐
                     │ Sentence Transformer    │
                     │ all-MiniLM-L6-v2        │
                     └──────────┬──────────────┘
                                │
                                ▼
                     ┌─────────────────────────┐
                     │ JD Embedding Vector     │
                     └──────────┬──────────────┘
                                │
                                │ Cosine Similarity
                                ▼
 ┌──────────────────────────────────────────────────────────┐
 │                 Candidate Database                       │
 │                                                          │
 │ • Profile Summary                                        │
 │ • Skills                                                  │
 │ • Career History                                          │
 │ • Current Role                                            │
 │ • Recruiter Signals                                       │
 └──────────────────────┬───────────────────────────────────┘
                        │
                        ▼
          ┌───────────────────────────────┐
          │ Precomputed Candidate         │
          │ Embeddings (.npy Cache)       │
          └───────────────┬───────────────┘
                          │
                          ▼
          ┌───────────────────────────────┐
          │ Semantic Matching Engine      │
          │ Cosine Similarity             │
          └───────────────┬───────────────┘
                          │
                          ▼
          ┌───────────────────────────────┐
          │ Hybrid Scoring Engine         │
          │                               │
          │ • Semantic Score              │
          │ • Career Relevance Score      │
          │ • Experience Score            │
          │ • Availability Score          │
          │ • Recruiter Signal Score      │
          └───────────────┬───────────────┘
                          │
                          ▼
          ┌───────────────────────────────┐
          │ Candidate Ranking             │
          │ Sort by Final Score           │
          └───────────────┬───────────────┘
                          │
                          ▼
          ┌───────────────────────────────┐
          │ Top Recommended Candidates    │
          │ + Explainable Reasons         │
          └───────────────────────────────┘
```

```

---

## 🧠 Ranking Methodology

RecruitAI uses a Hybrid AI Ranking Engine that combines semantic understanding with recruiter-centric signals.

### Stage 1: Semantic Understanding

The job description is converted into a dense embedding using Sentence Transformers.

Each candidate profile is represented using:

* Professional Summary
* Skills
* Career History
* Current Role

Cosine Similarity is then used to measure relevance between the Job Description and Candidate Profile.

### Stage 2: Career Relevance Analysis

Additional scoring is applied based on:

* Current Job Title
* Domain Relevance
* Years of Experience
* Historical Work Experience

This helps prioritize candidates whose career trajectory aligns with the target role.

### Stage 3: Recruiter Signal Scoring

RecruitAI incorporates behavioral and platform signals such as:

* GitHub Activity
* Recruiter Response Rate
* Interview Completion Rate
* Profile Completeness
* Saved By Recruiters
* Open To Work Status
* Offer Acceptance Rate



### Stage 4: Hybrid Candidate Ranking

Final Score =

Semantic Match Score

* Career Relevance Score
* Experience Score
* Recruiter Signal Score
* Availability Score

Candidates are ranked based on the final hybrid score and returned as an explainable shortlist.

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI / ML

- Sentence Transformers
- all-MiniLM-L6-v2
- Scikit-Learn
- Cosine Similarity

### Data Processing

- Pandas
- NumPy

---

## 📸 Screenshots

### Dashboard

<p align="center">
Add Screenshot Here
</p>

### Candidate Rankings

<p align="center">
Add Screenshot Here
</p>

### Recommendation Details

<p align="center">
Add Screenshot Here
</p>

---

## 📂 Project Structure

```text
RecruitAI/
│
├── backend/
│   ├── rank_candidates.py
│   ├── batch_ranker.py
│   ├── generate_submission.py
│   └── data/
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── submission.csv
└── README.md
```

---

## 📊 Dataset Features Used

- Candidate Summary
- Candidate Skills
- Job Title
- Experience
- GitHub Activity
- Recruiter Response Rate
- Interview Completion Rate
- Open To Work Status

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/harshitaojha123/RecruitAI.git
cd RecruitAI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
cd frontend
streamlit run app.py
```

---

## 📄 Output

The system produces:

✅ Ranked Candidate Shortlist

✅ Candidate Recommendation Dashboard

✅ submission.csv

---

## 🔮 Future Improvements

- FAISS Vector Search
- Pinecone Integration
- LLM Re-Ranking
- Resume Parsing
- Multi-Agent Recruitment Pipeline
- Explainable AI Dashboard

---

## 👩‍💻 Author

### Harshita Ojha

🚀 Software Developer

🧠 AI/ML Enthusiast

💻 MERN Stack Developer

🔗 GitHub: https://github.com/harshitaojha123

🔗 LinkedIn: https://www.linkedin.com/in/harshita-ojha-4970b4296/

---

<div align="center">

⭐ If you found this project interesting, please consider starring the repository ⭐

</div>


## 📊 Dataset Setup

⚠️ The original dataset is **not included in this repository** because it exceeds GitHub's file size limit (100 MB).

To run the project locally, download the dataset provided by the hackathon organizers and place:

`candidates.jsonl`

inside:

```text
backend/data/raw/
```

Expected structure:

```text
RecruitAI/
│
├── backend/
│   ├── data/
│   │   └── raw/
│   │       └── candidates.jsonl
│   │
│   └── rank_candidates.py
│
├── frontend/
│   └── app.py
│
└── README.md
```

Once the dataset is placed correctly, start the application using:

```bash
cd frontend
streamlit run app.py
```
