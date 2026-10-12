"""
EduPro Learner Demographics & Course Enrollment Behavior Analysis
Interactive Streamlit Dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="EduPro Learner Analytics",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    # Agar data folder me edupro.xlsx hai to ye path use karo
    data_path = Path(__file__).parent.parent / "data" / "edupro.xlsx"
    
    # Agar file kisi aur jagah hai to yahan path change karo
    # data_path = "edupro.xlsx"
    
    users = pd.read_excel(data_path, sheet_name="Users")
    courses = pd.read_excel(data_path, sheet_name="Courses")
    transactions = pd.read_excel(data_path, sheet_name="Transactions")

    def age_band(age):
        if age < 18:
            return "<18"
        elif age <= 25:
            return "18-25"
        else:
            return "26-35"

    users["AgeBand"] = users["Age"].apply(age_band)

    df = (
        transactions
        .merge(users[["UserID", "Age", "Gender", "AgeBand"]], on="UserID", how="left")
        .merge(
            courses[["CourseID", "CourseName", "CourseCategory", "CourseType", "CourseLevel"]],
            on="CourseID",
            how="left"
        )
    )
    return df, users, courses


df, users, courses = load_data()

# Sidebar Filters
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("---")

age_options = ["<18", "18-25", "26-35"]
age_filter = st.sidebar.multiselect("Age Band", options=age_options, default=age_options)
gender_filter = st.sidebar.multiselect("Gender", options=sorted(df["Gender"].unique()), default=list(df["Gender"].unique()))
cat_filter = st.sidebar.multiselect("Course Category", options=sorted(df["CourseCategory"].unique()), default=sorted(df["CourseCategory"].unique()))
level_filter = st.sidebar.multiselect("Course Level", options=["Beginner", "Intermediate", "Advanced"], default=["Beginner", "Intermediate", "Advanced"])
type_filter = st.sidebar.multiselect("Course Type", options=["Free", "Paid"], default=["Free", "Paid"])

filtered = df[
    (df["AgeBand"].isin(age_filter)) &
    (df["Gender"].isin(gender_filter)) &
    (df["CourseCategory"].isin(cat_filter)) &
    (df["CourseLevel"].isin(level_filter)) &
    (df["CourseType"].isin(type_filter))
].copy()

# Header
st.title("📚 EduPro Learner Analytics Dashboard")
st.markdown(
    "**Learner Demographics & Course Enrollment Behavior Analysis**  \n"
    "Unified Mentor × Toronto Government Parks, Forestry & Recreation | Analysis Year: 2025"
)
st.markdown("---")

# KPI Row
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Enrollments", f"{len(filtered):,}")
with col2:
    st.metric("Unique Learners", f"{filtered['UserID'].nunique():,}")
with col3:
    avg = len(filtered) / max(filtered["UserID"].nunique(), 1)
    st.metric("Avg Courses / Learner", f"{avg:.2f}")
with col4:
    female_pct = (filtered["Gender"] == "Female").mean() * 100 if len(filtered) > 0 else 0
    st.metric("Female Participation", f"{female_pct:.1f}%")
with col5:
    top_cat = filtered["CourseCategory"].value_counts().index[0] if len(filtered) > 0 else "—"
    st.metric("Top Category", top_cat)

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👥 Demographics",
    "📈 Enrollment Patterns",
    "🔥 Preference Heatmaps",
    "📊 Level & Type Deep Dive",
    "💡 Key Insights"
])

# TAB 1
with tab1:
    st.subheader("Learner Demographic Overview")
    c1, c2 = st.columns(2)

    with c1:
        age_order = ["<18", "18-25", "26-35"]
        fig = px.histogram(
            filtered, x="AgeBand", color="Gender", barmode="group",
            category_orders={"AgeBand": age_order},
            title="Enrollments by Age Band & Gender",
            color_discrete_map={"Female": "#E91E63", "Male": "#2196F3"},
            labels={"count": "Enrollments", "AgeBand": "Age Band"}
        )
        fig.update_layout(height=420)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig = px.pie(
            filtered, names="Gender", title="Gender Participation Share",
            hole=0.45, color="Gender",
            color_discrete_map={"Female": "#E91E63", "Male": "#2196F3"}
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(height=420)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Unique Learners by Age Band")
    learner_age = (
        filtered.groupby("AgeBand")["UserID"].nunique()
        .reindex(age_order).reset_index(name="Unique Learners")
    )
    fig = px.bar(
        learner_age, x="AgeBand", y="Unique Learners", text="Unique Learners",
        title="Unique Learners per Age Band", color="AgeBand",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

# TAB 2
with tab2:
    st.subheader("Course Enrollment Distribution")
    c1, c2 = st.columns(2)

    with c1:
        cat_counts = (
            filtered["CourseCategory"].value_counts().reset_index()
            .rename(columns={"count": "Enrollments", "CourseCategory": "Category"})
        )
        fig = px.bar(
            cat_counts, x="Enrollments", y="Category", orientation="h",
            title="Category Popularity", color="Enrollments",
            color_continuous_scale="Blues"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"}, height=500)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig = px.pie(
            filtered, names="CourseLevel", title="Course Level Preference",
            hole=0.4, color="CourseLevel",
            color_discrete_map={"Beginner": "#4CAF50", "Intermediate": "#FF9800", "Advanced": "#F44336"},
            category_orders={"CourseLevel": ["Beginner", "Intermediate", "Advanced"]}
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Free vs Paid Enrollments")
    type_counts = filtered["CourseType"].value_counts().reset_index()
    type_counts.columns = ["Type", "Enrollments"]
    fig = px.bar(
        type_counts, x="Type", y="Enrollments", color="Type", text="Enrollments",
        title="Free vs Paid Course Enrollments",
        color_discrete_map={"Free": "#00BCD4", "Paid": "#9C27B0"}
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

# TAB 3
with tab3:
    st.subheader("Demographics × Course Preference Heatmaps")

    heat1 = pd.crosstab(filtered["AgeBand"], filtered["CourseCategory"], normalize="index") * 100
    heat1 = heat1.reindex(["<18", "18-25", "26-35"])

    fig = px.imshow(
        heat1.round(1), text_auto=".1f", aspect="auto",
        title="Age Band vs Course Category (% within each Age Band)",
        color_continuous_scale="Blues",
        labels=dict(x="Course Category", y="Age Band", color="% Share")
    )
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        heat2 = pd.crosstab(filtered["Gender"], filtered["CourseLevel"], normalize="index") * 100
        fig = px.imshow(
            heat2.round(1), text_auto=".1f", aspect="auto",
            title="Gender vs Course Level (% within Gender)",
            color_continuous_scale="Greens",
            labels=dict(x="Course Level", y="Gender", color="% Share")
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        heat3 = pd.crosstab(filtered["AgeBand"], filtered["CourseLevel"], normalize="index") * 100
        heat3 = heat3.reindex(["<18", "18-25", "26-35"])
        fig = px.imshow(
            heat3.round(1), text_auto=".1f", aspect="auto",
            title="Age Band vs Course Level (% within Age Band)",
            color_continuous_scale="Oranges",
            labels=dict(x="Course Level", y="Age Band", color="% Share")
        )
        st.plotly_chart(fig, use_container_width=True)

# TAB 4
with tab4:
    st.subheader("Level Preference by Demographic Segment")

    level_age = filtered.groupby(["AgeBand", "CourseLevel"]).size().reset_index(name="Enrollments")
    fig = px.bar(
        level_age, x="AgeBand", y="Enrollments", color="CourseLevel", barmode="group",
        category_orders={"AgeBand": ["<18", "18-25", "26-35"], "CourseLevel": ["Beginner", "Intermediate", "Advanced"]},
        color_discrete_map={"Beginner": "#4CAF50", "Intermediate": "#FF9800", "Advanced": "#F44336"},
        title="Course Level Enrollments by Age Band"
    )
    st.plotly_chart(fig, use_container_width=True)

    level_gender = filtered.groupby(["Gender", "CourseLevel"]).size().reset_index(name="Enrollments")
    fig = px.bar(
        level_gender, x="Gender", y="Enrollments", color="CourseLevel", barmode="group",
        category_orders={"CourseLevel": ["Beginner", "Intermediate", "Advanced"]},
        color_discrete_map={"Beginner": "#4CAF50", "Intermediate": "#FF9800", "Advanced": "#F44336"},
        title="Course Level Enrollments by Gender"
    )
    st.plotly_chart(fig, use_container_width=True)

# TAB 5
with tab5:
    st.subheader("💡 Key Behavioral Insights & Recommendations")
    st.markdown("""
    ### Core Findings (Full Dataset)

    | Insight | Detail |
    |---------|--------|
    | **Dominant Age Cohort** | 26–35 age band drives **48.0%** of all enrollments |
    | **Gender Balance** | Near parity — Female **50.8%** / Male **49.2%** |
    | **Level Preference** | Beginner 35.7% ≈ Advanced 34.8% > Intermediate 29.5% |
    | **Top Categories** | Data Science, Finance, Web Development, Business, AI |
    | **Free vs Paid** | Free courses account for **64%** of enrollments |
    | **Engagement Depth** | Average **3.33** courses per learner |

    ### Strategic Recommendations
    1. **Strengthen Intermediate Pathways** – Create clearer bridge modules.
    2. **Prioritize 26–35 Content** – Focus career-oriented offerings.
    3. **Preserve Gender Parity** – Continue inclusive messaging.
    4. **Design Learning Paths** – Capitalize on 3.3 average courses/learner.
    5. **Under-18 Engagement** – Develop age-appropriate introductory pathways.
    """)
    st.success("Use the sidebar filters to explore any specific demographic or course segment in real time.")

st.markdown("---")
st.caption("EduPro Learner Analytics Dashboard | Unified Mentor × Toronto Government Parks, Forestry & Recreation | 2025 Data")