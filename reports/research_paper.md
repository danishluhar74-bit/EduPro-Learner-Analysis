# EduPro Learner Demographics and Course Enrollment Behavior Analysis

**A Descriptive Analytics Study**

**Guided by:** Unified Mentor  
**Submitted to:** Toronto Government Parks, Forestry & Recreation  
**Analysis Year:** 2025  
**Date:** March 2026  

---

## 1. Abstract

This study presents a comprehensive descriptive analysis of learner demographics and course enrollment behavior on the EduPro online learning platform. Using data from 3,000 registered learners, 60 courses spanning 12 subject categories, and 10,000 enrollment transactions recorded in 2025, the research answers fundamental questions about who participates and how they choose courses. Key findings show that the 26–35 age group constitutes the largest active segment (48.0% of enrollments), female learners hold a marginal participation majority at 50.8%, and Beginner-level courses are slightly preferred (35.7%). Data Science emerges as the most popular category. The analysis provides actionable intelligence for course design, targeted outreach, and inclusive platform growth without venturing into predictive modeling or monetization.

**Keywords:** Learning Analytics, Learner Demographics, Course Enrollment Behavior, Educational Data Mining, Descriptive Analytics

---

## 2. Introduction and Problem Statement

Online learning platforms serve diverse populations with varying ages, genders, goals, and subject interests. For EduPro, understanding learner composition and enrollment patterns is foundational for:

- Designing relevant and progressive courses
- Improving engagement and retention
- Conducting targeted marketing and outreach
- Enhancing inclusivity and accessibility

Despite possessing rich user and transaction data, EduPro previously lacked clear answers to:

- Which age groups are most active?
- How do enrollment patterns differ by gender?
- Which course categories attract different learner segments?
- Are Beginner, Intermediate, or Advanced courses preferred by specific age groups?

Without these insights, decisions remained largely intuition-driven. This project delivers systematic descriptive learner intelligence to close that gap.

---

## 3. Dataset Description

### 3.1 Data Sources

| Sheet        | Records | Fields Utilized                                      |
|--------------|---------|------------------------------------------------------|
| Users        | 3,000   | UserID, UserName, Age, Gender                        |
| Courses      | 60      | CourseID, CourseName, CourseCategory, CourseType, CourseLevel |
| Transactions | 10,000  | TransactionID, UserID, CourseID, TransactionDate     |

### 3.2 Data Quality and Integration

Data integration was performed via inner joins on `UserID` (Users ↔ Transactions) and `CourseID` (Transactions ↔ Courses). Referential integrity was verified: all transaction UserIDs and CourseIDs exist in the respective master tables. Ages range from 15 to 35. No missing values were present in the analytically relevant fields.

### 3.3 Derived Features

Learners were segmented into age bands:
- **<18**
- **18–25**
- **26–35**

(Note: The dataset maximum age is 35; higher bands were not required.)

---

## 4. Methodology

### 4.1 Analytical Framework

1. **Data Integration** – Join Users, Transactions, and Courses.
2. **Learner Demographic Analysis** – Age-band distribution, gender ratios, participation levels.
3. **Enrollment Distribution Analysis** – Counts by CourseCategory, CourseType, and CourseLevel.
4. **Demographics × Preference Analysis** – Cross-tabulations and heatmaps (Age × Category, Gender × Level, etc.).
5. **Behavioral Metrics** – Average courses per learner, concentration, level preference consistency.

### 4.2 Key Performance Indicators (KPIs)

| KPI Name                      | Description                          |
|-------------------------------|--------------------------------------|
| Total Enrollments             | Overall platform engagement          |
| Enrollments by Age Group      | Demographic reach                    |
| Gender Participation Ratio    | Inclusivity metric                   |
| Category Popularity Index     | Course demand                        |
| Level Preference Distribution | Skill-maturity insight               |
| Average Courses per Learner   | Depth of engagement                  |

---

## 5. Results

### 5.1 Age Distribution

| Age Band | Unique Learners | % of Learners | Enrollments | % of Enrollments |
|----------|-----------------|---------------|-------------|------------------|
| <18      | 433             | 14.4%         | 1,469       | 14.7%            |
| 18–25    | 1,121           | 37.4%         | 3,732       | 37.3%            |
| 26–35    | 1,446           | 48.2%         | 4,799       | 48.0%            |
| **Total**| **3,000**       | **100%**      | **10,000**  | **100%**         |

The 26–35 cohort is the clear dominant segment.

### 5.2 Gender Participation

- Learners: Female 50.7% (1,520) / Male 49.3% (1,480)
- Enrollments: Female 50.8% / Male 49.2%

Near parity indicates strong inclusivity.

### 5.3 Course Level Preference

| Level         | Enrollments | Share  |
|---------------|-------------|--------|
| Beginner      | 3,573       | 35.7%  |
| Advanced      | 3,475       | 34.8%  |
| Intermediate  | 2,952       | 29.5%  |

Beginner and Advanced are nearly equal; Intermediate shows a relative dip.

### 5.4 Category Popularity (Top 10)

1. Data Science – 916  
2. Finance – 864  
3. Web Development – 844  
4. Business – 833  
5. Project Management – 829  
6. Artificial Intelligence – 829  
7. Design – 827  
8. Cybersecurity – 819  
9. Machine Learning – 819  
10. Digital Marketing – 808  

### 5.5 Course Type

- Free: 64.0%  
- Paid: 36.0%

### 5.6 Cross-Segment Insights

- Level preference is remarkably consistent across all three age bands and both genders.
- No dramatic gender divergence in category or level choice was observed.
- Average courses per learner = **3.33**.

---

## 6. Discussion and Behavioral Insights

1. **Mature Working-Age Dominance**  
   The 26–35 group’s leadership aligns with career-upskilling motivations typical of this life stage.

2. **Healthy Gender Balance**  
   The near 50/50 split is a positive inclusivity signal that should be actively preserved.

3. **Intermediate Dip**  
   The lower Intermediate share may indicate either a preference for jumping from Beginner to Advanced or a gap in intermediate offerings. This warrants curriculum review.

4. **Free-Course Preference**  
   64% free enrollments highlight the importance of freemium models for acquisition while still generating substantial paid activity (36%).

5. **Multi-Course Engagement**  
   An average of 3.33 courses per learner creates a natural opportunity for sequenced learning paths and progressive recommendations.

---

## 7. Recommendations

### Course Design
- Build clearer Intermediate pathways and bridge modules.
- Expand high-demand categories (Data Science, AI, Finance, Web Development).
- Create age-appropriate entry points for the under-18 segment.

### Marketing & Outreach
- Prioritize the 26–35 segment for advanced and career-oriented content.
- Maintain gender-neutral messaging while monitoring technical category balance.
- Use free courses strategically as funnels into paid pathways.

### Platform Growth
- Design multi-course learning journeys that capitalize on the 3.3 average enrollment depth.
- Continuously monitor Intermediate completion and transition rates.
- Preserve and celebrate the current gender parity as a core platform strength.

---

## 8. Conclusion

This project delivers foundational learner intelligence for EduPro. By systematically analyzing who learners are and how they enroll, the platform can transition from intuition-based to data-driven education planning. The insights ensure that course offerings, marketing strategies, and growth initiatives remain aligned with actual learner needs, preferences, and diversity.

---

## 9. References

1. EduPro Online Platform Dataset (2025). Internal transaction and user records. Sheets: Users, Courses, Transactions.
2. Unified Mentor Project Guidelines – Learner Demographics and Course Enrollment Behavior Analysis.
3. Toronto Government Parks, Forestry & Recreation – Stakeholder requirements for inclusive digital learning insights.

---

*End of Research Paper*