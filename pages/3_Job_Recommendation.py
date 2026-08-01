import streamlit as st
import pandas as pd
from resume_parser import read_pdf
from skills import extract_skills

st.set_page_config(
    page_title="Job Recommendation",
    page_icon="💼"
)

st.title("💼 Job Recommendation")
st.write("Upload your resume to get personalized job recommendations.")

# Load Job Database
try:
    jobs = pd.read_excel("job_database.xlsx", engine="openpyxl")
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# Resume Upload
uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_resume is not None:

    resume_text = read_pdf(uploaded_resume)
    resume_skills = extract_skills(resume_text)

    st.success("✅ Resume uploaded successfully!")

    st.divider()

    st.subheader("Job Matching Results")

    recommendations = []

    # Compare resume with every job
    for _, job in jobs.iterrows():

        job_skills = job["Required Skills"].split(",")

        job_skills = [skill.strip().lower() for skill in job_skills]

        matched = set(resume_skills) & set(job_skills)

        match_percentage = round(
            (len(matched) / len(job_skills)) * 100,
            2
        )

        recommendations.append({
            "Company": job["Company Name"],
            "Role": job["Job Role"],
            "Location": job["Location"],
            "Salary": job["Salary"],
            "Experience": job["Experience"],
            "Openings": job["No of Openings"],
            "Learning Resource": job["Learning Resource"],
            "Score": match_percentage
})
    # ✅ Sort first
    recommendations.sort(
        key=lambda x: x["Score"],
        reverse=True
    )

    # ✅ Create top_jobs
    top_jobs = recommendations[:3]

    # ✅ Then display them
    st.markdown("###### Top 3 Recommended Jobs")

    for job in top_jobs:

        with st.expander(
            f"🏢 {job['Company']} ({job['Location']}) - {job['Role']}   🎯 {job['Score']}%"
        ):

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("💰 Salary")
                st.write(job["Salary"])

            with col2:
                st.write("👨‍💻 Experience")
                st.write(job["Experience"])

            with col3:
                st.write("📌 Openings")
                st.write(job["Openings"])

            st.markdown("---")

            st.write("###### 📚 Recommendation")

            if job["Score"] >= 90:

                st.success(f"""
            Excellent Match!
            Your resume matches **{job['Score']}%** of the required skills.
            You are highly suitable for this position.
            We recommend applying for this job.""")

            elif job["Score"] >= 70:

                st.info(f"""
            Strong Match!
            Your resume matches **{job['Score']}%** of the required skills.
            You only need to improve a few missing skills.
            Suggested Learning Resource:{job["Learning Resource"]}""")

            elif job["Score"] >= 40:

                st.warning(f"""
            Moderate Match
            Your resume matches **{job['Score']}%** of the required skills.
            You should improve your technical skills before applying.
            Suggested Learning Resource:{job["Learning Resource"]}""")

            else:

                st.error(f"""
            Low Match
            Your resume matches only **{job['Score']}%** of the required skills.
            We recommend learning the missing skills and building a few projects before applying.
            Suggested Learning Resource:{job["Learning Resource"]}""")