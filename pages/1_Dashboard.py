import streamlit as st
import matplotlib.pyplot as py 

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊"
)

st.title("📊 Dashboard")
st.write("Welcome to your AI Career Assistant Dashboard!")

st.divider()

if not st.session_state.analysis_done:
    st.info("📄 Analyze your resume first to view your dashboard statistics.")
else:
    col1, col2 = st.columns(2)

    with col1:
        st.metric("🎯 ATS Score", f"{st.session_state.ats_score}%")

    with col2:
        st.metric("📄 Resume Skills", st.session_state.resume_skills)

    col3, col4 = st.columns(2)

    with col3:
        st.metric("✅ Matching Skills", st.session_state.matching_skills)

    with col4:
        st.metric("❌ Missing Skills", st.session_state.missing_skills)

    st.divider()

    st.subheader("💡 Career Recommendation")
    score = st.session_state.ats_score

    if score >= 80:
        st.success("Excellent Match!")
        st.write("""
        Your resume matches the job requirements very well.

    ### Next Steps:
    - ✅ Apply for this job confidently.
    - ✅ Tailor your resume for the company.
    - ✅ Keep your projects and certifications updated.""")

    elif score >= 50:
        st.warning("👍 Good Match")

        st.write("""
    Your resume is a good match, but there is room for improvement.

    ### Next Steps:
    - ✅ Add the missing technical skills.
    - ✅ Include more relevant projects.
    - ✅ Customize your resume according to the job description.""")

    else:
        st.error("📈 Needs Improvement")

        st.write("""
    Your resume currently has a low match with the job description.

    ### Next Steps:
    - ✅ Learn the missing skills.
    - ✅ Update your resume with relevant projects.
    - ✅ Add certifications if available.
    - ✅ Apply after improving your resume.""")

    st.subheader("📌 Missing Skills")

    if st.session_state.missing_skills_list:
        for skill in st.session_state.missing_skills_list:
            st.error(f"• {skill}")
    else:
        st.success("No missing skills found!")

    st.divider()

    st.subheader("📊 Skills Overview")
    fig, ax = py.subplots()
    labels = ["Matching Skills", "Missing Skills"]

    sizes = [
        st.session_state.matching_skills,
        st.session_state.missing_skills
    ]
    ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#4CAF50","#F44336"]
    )
    ax.set_title("Resume Skill Match")
    ax.axis("equal")
    st.pyplot(fig)