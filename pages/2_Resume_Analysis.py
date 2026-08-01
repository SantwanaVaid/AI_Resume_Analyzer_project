import streamlit as st

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

from resume_parser import read_pdf
from similarity import calculate_similarity
from skills import extract_skills

st.title("📄 Resume Analysis")
st.write("Upload your resume and compare it with a job description using AI.")
st.subheader("📤 Upload Resume")

upload_file = st.file_uploader(
    "Choose your PDF Resume",
    type=["pdf"]
)

st.subheader("📋 Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=200
)

st.divider()

if st.button("Analyze Resume", use_container_width=True):
    if upload_file is not None:
        with st.spinner("Analyzing your resume ..."):

            resume_text = read_pdf(upload_file)
            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_description)

            matching = set(resume_skills) & set(job_skills)

        if len(job_skills) > 0:
            similarity = round((len(matching) / len(job_skills)) * 100, 2)
        else:
            similarity = 0

        st.session_state.analysis_done = True
        st.session_state.ats_score = similarity
        st.session_state.resume_skills = len(resume_skills)

        st.success("✅ Resume uploaded and analyzed successfully!")
        st.divider()

        st.header("📊 Analysis Results")

        resume_col, job_col = st.columns(2)

        with resume_col:
            st.subheader("📄 Resume Skills")
            for skill in resume_skills:
                st.success(f"📌 {skill}")

        with job_col:
            st.subheader("💼 Job Skills")
            for skill in job_skills:
                st.info(f"📌 {skill}")

        st.subheader("Skill Statistics")

        matched = list(set(resume_skills) & set(job_skills))
        missing = list(set(job_skills) - set(resume_skills))

        st.session_state.matching_skills = len(matched)
        st.session_state.missing_skills = len(missing)

        st.session_state.matched_skills_list = matched
        st.session_state.missing_skills_list = missing

        st.subheader("📈 Skill Statistics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Resume Skills", len(resume_skills))

        with col2:
            st.metric("Job Skills", len(job_skills))

        with col3:
            st.metric("Matched", len(matched))

        with col4:
            st.metric("Missing", len(missing))

        match_col, miss_col = st.columns(2)

        with match_col:
            st.subheader("✅ Matching Skills")

            if matched:
                for skill in matched:
                    st.success(skill)
            else:
                st.info("No matching skills found.")

        with miss_col:
            st.subheader("❌ Missing Skills")

            if missing:
                for skill in missing:
                    st.error(skill)
            else:
                st.success("No missing skills 🎉")
        st.subheader("🎯 ATS Match Score")

        st.progress(similarity / 100)

        st.metric(
            label="Overall Match",
             value=f"{similarity}%"
        )

        if similarity >= 80:
            st.success("Excellent Match! Your resume is highly suitable for this job.")

        elif similarity >= 50:
            st.warning("Good Match! You can improve your resume by adding a few more relevant skills.")

        else:
            st.error("Low Match! Consider adding the missing skills to improve your resume.")

    else:
        st.error("⚠️ Please upload a PDF resume first.")

st.markdown("---")

st.caption("Developed using Python • Streamlit • PyPDF2 • AI-based Skill Matching")