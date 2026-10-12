# EduPro Learner Demographics & Course Enrollment Behavior Analysis

**Descriptive Analytics Project**  
**Guided by:** Unified Mentor  
**Submitted to:** Toronto Government Parks, Forestry & Recreation  
**Analysis Year:** 2025

---

## Project Overview

This project analyzes learner demographics and course enrollment behavior on the **EduPro** online learning platform.  
It answers key questions about:

- Who the learners are (Age & Gender)
- How they enroll in courses
- Which categories and levels are most preferred
- Behavioral patterns across different learner segments

**Scope:** Descriptive Analysis + Interactive Dashboard (No prediction/monetization focus)

---

## Dataset

| Sheet        | Records | Key Fields                                      |
|--------------|---------|-------------------------------------------------|
| Users        | 3,000   | UserID, Age, Gender                             |
| Courses      | 60      | CourseID, CourseCategory, CourseType, CourseLevel |
| Transactions | 10,000  | TransactionID, UserID, CourseID, TransactionDate |

---

## Key Findings

| Metric                        | Value                          |
|-------------------------------|--------------------------------|
| Total Enrollments             | 10,000                         |
| Unique Learners               | 3,000                          |
| Avg Courses per Learner       | 3.33                           |
| Dominant Age Band             | 26–35 (48.0% of enrollments)   |
| Gender Balance                | Female 50.8% / Male 49.2%      |
| Most Popular Level            | Beginner (35.7%)               |
| Top Categories                | Data Science, Finance, Web Dev |
| Free vs Paid                  | Free 64% / Paid 36%            |

---

## Project Structure
EduPro_Learner_Analysis/
├── app/
│   └── streamlit_app.py          # Interactive Dashboard
├── data/
│   └── edupro.xlsx               # Dataset
├── notebooks/
│   └── 01_EDA_Learner_Analysis.ipynb
├── reports/
│   ├── research_paper.md
│   └── executive_summary.md
├── requirements.txt
└── README.md


---

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt

streamlit run app/streamlit_app.py

jupyter notebook notebooks/01_EDA_Learner_Analysis.ipynb

```
Features of Dashboard

Live KPIs (Total Enrollments, Unique Learners, Avg Courses, Gender Share)
Age Band & Gender filters
Course Category, Level & Type filters
Interactive charts & heatmaps
Demographic vs Preference analysis
Key insights & recommendations


Deliverables

Research Paper (EDA + Insights + Recommendations)
Interactive Streamlit Dashboard
Executive Summary for stakeholders
Full reproducible Jupyter Notebook
Optional K-Means learner segmentation


Technologies Used

Python
Pandas, NumPy
Matplotlib, Seaborn, Plotly
Streamlit
Scikit-learn (K-Means clustering)
Jupyter Notebook

Author
Danish Luhar

GitHub: danishluhar74-bit

License
This project is created for educational purposes under Unified Mentor guidance.


---

### 2. README update karke GitHub pe bhejo

Git Bash me ye chalao:

```bash
cd /c/Users/ASUS/Desktop/EduPro_Learner_Analysis
git add README.md
git commit -m "Updated professional README"
git push
```
