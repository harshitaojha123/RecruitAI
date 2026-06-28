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
Job Description
       │
       ▼
Sentence Transformer
       │
       ▼
JD Embedding Vector
       │
       ▼
Candidate Profiles
       │
       ▼
Candidate Embeddings
       │
       ▼
Hybrid Scoring Engine
       │
       ▼
Candidate Ranking
       │
       ▼
Top Recommended Candidates
```

---

## 🧠 Ranking Methodology

### 1️⃣ Semantic Similarity

Measures relevance between:

- Job Description
- Candidate Summary
- Candidate Skills

Using:

- Sentence Transformers
- Cosine Similarity

### 2️⃣ Experience Score

Additional weighting based on:

- Years of Experience
- Career Relevance

### 3️⃣ Recruiter Signals

Includes:

- GitHub Activity Score
- Recruiter Response Rate
- Interview Completion Rate
- Open To Work Status

### 4️⃣ Final Hybrid Score

```python
Final Score =
Semantic Score
+ Experience Score
+ GitHub Activity Score
+ Recruiter Response Score
+ Interview Completion Score
+ Open To Work Bonus
```

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
