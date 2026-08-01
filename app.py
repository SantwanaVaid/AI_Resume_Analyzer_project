import streamlit as st

# Initialize session state
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <h1 style='text-align:center;color:#4F46E5;'>
    🤖 AI Career Assistant
    </h1>

    <h3 style='text-align:center;color:gray;'>
    Analyze • Improve • Get Hired
    </h3>

    <p style='text-align:center;font-size:20px;'>
    Your Personal AI Career Coach
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# (Feature cards will go here)
# ---------- First Row ----------
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("📄 Resume Analysis")
        st.write("Analyze your resume with AI.")
        if st.button("Open", key="resume"):
            st.switch_page("pages/2_Resume_Analysis.py")

with col2:
    with st.container(border=True):
        st.subheader("📊 Dashboard")
        st.write("View your analysis and progress.")
        if st.button("Open", key="dashboard"):
            st.switch_page("pages/1_Dashboard.py")


st.write("")


# ---------- Second Row ----------
col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("💼 Job Recommendation")
        st.write("Find jobs that match your skills.")
        if st.button("Open", key="job"):
            st.switch_page("pages/3_Job_Recommendation.py")

with col4:
    with st.container(border=True):
        st.subheader("🎯 Interview Preparation")
        st.write("Practice technical and HR interviews.")
        if st.button("Open", key="interview"):
            st.switch_page("pages/4_Interview_Preparation.py")


st.write("")


# ---------- Third Row ----------
col5, col6, col7 = st.columns([1,2,1])

with col6:
    with st.container(border=True):
        st.subheader("✉️ Cover Letter Generator")
        st.write("Generate a professional cover letter.")
        if st.button("Open", key="cover"):
            st.switch_page("pages/5_Cover_Letter_Generator.py")
st.divider()

st.caption("Developed by Santwana Vaid | Version 1.0")