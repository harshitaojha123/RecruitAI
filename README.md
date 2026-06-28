<<<<<<< HEAD
# RecruitAI 🤖

AI-Powered Candidate Discovery & Ranking System

## Overview

RecruitAI helps recruiters identify the best candidates by understanding the meaning of a Job Description instead of relying solely on keyword matching.

The system combines semantic search, candidate skills, career history, experience, and recruiter activity signals to generate a ranked shortlist of candidates.

---

## Features

* Semantic Job Description Understanding
* AI-Powered Candidate Ranking
* Hybrid Scoring Model
* Career History Analysis
* Recruiter Signal Integration
* Explainable Recommendations
* Streamlit Dashboard
* CSV Submission Generation

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / ML

* Sentence Transformers
* all-MiniLM-L6-v2
* Cosine Similarity

### Data Processing

* Pandas
* NumPy

### Machine Learning Libraries

* Scikit-Learn

---

## Architecture

Job Description
↓
Sentence Transformer Embedding
↓
Candidate Embeddings
↓
Hybrid Scoring Engine
↓
Candidate Ranking
↓
Top 10 Recommended Candidates

---

## UI Screenshots

### Dashboard

(Add Screenshot Here)

### Candidate Ranking Results

(Add Screenshot Here)

### Why Recommended Section

(Add Screenshot Here)

---

## Scoring Methodology

Final Score =

* Semantic Similarity
* Experience Score
* GitHub Activity Score
* Recruiter Response Rate
* Interview Completion Rate
* Open To Work Signal

---

## Dataset Fields Used

* Profile Summary
* Skills
* Career History
* Years of Experience
* GitHub Activity Score
* Recruiter Response Rate
* Interview Completion Rate
* Open To Work Flag

---

## How To Run

### Clone Repository

```bash
git clone <repo-url>
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

## Output

The system generates:

* Ranked Candidate List
* Explainable Recommendations
* submission.csv

---

## Future Improvements

* Vector Database Integration
* LLM Re-ranking
* Resume Parsing
* Multi-stage Retrieval Pipeline
* Advanced Explainable AI Ranking
=======
# RecruitAI
RecruitAI is an AI-powered candidate discovery and ranking system that helps recruiters identify the most relevant candidates by understanding job requirements semantically rather than relying solely on keyword matching. The platform analyzes candidate profiles using skills, career history, experience, recruiter activity signals.
>>>>>>> e024b67cea045ee391be6262c5777122116f2fdf
