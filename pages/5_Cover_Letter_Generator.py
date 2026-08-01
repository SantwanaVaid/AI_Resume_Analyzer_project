import streamlit as st
from ai_helper import generate_response

st.set_page_config(
    page_title="Cover Letter Generator",
    page_icon="✉️",
    layout="wide"
)

st.title("✉️ Cover Letter Generator")

st.write("Generate a professional cover letter using AI.")

job_role = st.text_input(
    "Job Role",
    placeholder="Python Developer"
)

company = st.text_input(
    "Company Name",
    placeholder="Google"
)

name = st.text_input(
    "Your Name",
    placeholder="XYZ"
)

skills = st.text_area(
    "Your Skills",
    placeholder="Python, SQL, Machine Learning, Streamlit"
)
if st.button("Generate Cover Letter"):

    prompt = f"""
Write a professional cover letter.

Candidate Name:
{name}

Job Role:
{job_role}

Company:
{company}

Skills:
{skills}

The cover letter should be professional, concise, and ready to send.
"""

    with st.spinner("Generating Cover Letter..."):
        cover_letter = generate_response(prompt)

    st.success("Cover Letter Generated!")

    st.text_area(
        "Your Cover Letter",
        cover_letter,
        height=450
    )