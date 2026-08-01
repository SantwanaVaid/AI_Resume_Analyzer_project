def extract_skills(text):
    skills = [
        "python",
        "java",
        "c++",
        "html",
        "css",
        "javascript",
        "sql",
        "mysql",
        "machine learning",
        "artificial intelligence",
        "deep learning",
        "tensorflow",
        "pandas",
        "numpy",
        "streamlit",
        "opencv",
        "git",
        "github",
        "data analysis"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills