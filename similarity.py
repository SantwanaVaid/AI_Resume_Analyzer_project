from difflib import SequenceMatcher

def calculate_similarity(resume_text, job_description):
    similarity = SequenceMatcher(
        None,
        resume_text.lower(),
        job_description.lower()
    ).ratio()

    return round(similarity * 100, 2)