import streamlit as st
from ai_helper import generate_response

st.set_page_config(
    page_title="Interview Preparation",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Interview Preparation")
st.write("Practice AI-generated interview questions.")

# ---------------- Session State ---------------- #

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current" not in st.session_state:
    st.session_state.current = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ---------------- Input ---------------- #

job_role = st.text_input(
    "Enter Job Role",
    placeholder="Python Developer"
)

skills = st.text_area(
    "Enter Your Skills",
    placeholder="Python, SQL, Machine Learning, Streamlit"
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

num_questions = st.slider(
    "Number of Questions",
    5,
    20,
    10
)

# ---------------- Generate Questions ---------------- #

if st.button("Generate Questions"):

    prompt = f"""
Generate {num_questions} interview questions.

Job Role:
{job_role}

Skills:
{skills}

Difficulty:
{difficulty}

Return ONLY numbered questions.
"""

    with st.spinner("Generating Questions..."):
        result = generate_response(prompt)

    st.session_state.questions = [
        q.strip()
        for q in result.split("\n")
        if q.strip()
    ]

    st.session_state.current = 0
    st.session_state.feedback = ""
    st.session_state.submitted = False

    st.rerun()

# ---------------- Interview ---------------- #

if len(st.session_state.questions) > 0:

    current = st.session_state.current

    if current < len(st.session_state.questions):

        st.subheader(f"Question {current+1}")

        st.write(st.session_state.questions[current])

        answer = st.text_area(
            "Your Answer",
            key=f"answer_{current}",
            height=180
        )

        if not st.session_state.submitted:

            if st.button("Submit Answer"):

                prompt = f"""
You are an expert interview evaluator.

Question:
{st.session_state.questions[current]}

Candidate Answer:
{answer}

Evaluate the answer.

Return:

1. Score out of 10

2. Strengths

3. Weaknesses

4. Correct Answer
"""

                with st.spinner("Evaluating Answer..."):
                    feedback = generate_response(prompt)

                st.session_state.feedback = feedback
                st.session_state.submitted = True

                st.rerun()

        if st.session_state.submitted:

            st.subheader("🤖 AI Feedback")

            st.write(st.session_state.feedback)

            if st.button("Next Question ➡️"):

                st.session_state.current += 1
                st.session_state.submitted = False
                st.session_state.feedback = ""

                st.rerun()

    else:

        st.success("🎉 Interview Completed!")

        st.write("Excellent! You have completed all interview questions.")

        if st.button("Start New Interview"):

            st.session_state.questions = []
            st.session_state.current = 0
            st.session_state.feedback = ""
            st.session_state.submitted = False

            st.rerun()