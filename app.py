import streamlit as st
import re
from PyPDF2 import PdfReader
from docx import Document

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Skills Database
# -----------------------------
SKILLS = {
    "Python": ["python"],
    "Java": ["java"],
    "C": ["c programming", "c language"],
    "C++": ["c++"],
    "JavaScript": ["javascript"],
    "HTML": ["html"],
    "CSS": ["css"],
    "SQL": ["sql", "mysql", "postgresql"],
    "Machine Learning": ["machine learning", "ml"],
    "Deep Learning": ["deep learning"],
    "Artificial Intelligence": ["artificial intelligence", "ai"],
    "Data Science": ["data science"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Git": ["git", "github"],
    "Django": ["django"],
    "Flask": ["flask"],
    "React": ["react", "reactjs"],
    "Cloud": ["aws", "azure", "cloud"],
    "Communication": ["communication"],
    "Leadership": ["leadership"],
    "Problem Solving": ["problem solving"]
}

# -----------------------------
# Extract PDF Text
# -----------------------------
def extract_pdf_text(file):
    text = ""

    reader = PdfReader(file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# -----------------------------
# Extract DOCX Text
# -----------------------------
def extract_docx_text(file):
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


# -----------------------------
# Extract Resume Text
# -----------------------------
def extract_resume_text(file):
    if file.name.lower().endswith(".pdf"):
        return extract_pdf_text(file)

    elif file.name.lower().endswith(".docx"):
        return extract_docx_text(file)

    return ""


# -----------------------------
# Find Skills
# -----------------------------
def find_skills(text):

    text = text.lower()

    found_skills = []

    for skill, keywords in SKILLS.items():

        for keyword in keywords:

            if keyword.lower() in text:
                found_skills.append(skill)
                break

    return found_skills


# -----------------------------
# Detect Sections
# -----------------------------
def check_sections(text):

    text_lower = text.lower()

    sections = {
        "Contact Information": [
            "email",
            "phone",
            "mobile"
        ],

        "Summary / Objective": [
            "summary",
            "objective",
            "profile"
        ],

        "Education": [
            "education",
            "qualification",
            "academic"
        ],

        "Experience": [
            "experience",
            "work experience",
            "employment"
        ],

        "Skills": [
            "skills",
            "technical skills"
        ],

        "Projects": [
            "projects",
            "project"
        ],

        "Certifications": [
            "certification",
            "certifications"
        ]
    }

    result = {}

    for section, keywords in sections.items():

        found = any(keyword in text_lower for keyword in keywords)

        result[section] = found

    return result


# -----------------------------
# Calculate Resume Score
# -----------------------------
def calculate_score(text, skills, sections):

    score = 0

    # Skills score
    skill_score = min(len(skills) * 3, 30)

    # Section score
    section_score = sum(sections.values()) * 5

    # Resume length
    word_count = len(text.split())

    if word_count >= 400:
        length_score = 15
    elif word_count >= 250:
        length_score = 10
    elif word_count >= 100:
        length_score = 5
    else:
        length_score = 0

    # Contact information
    contact_score = 10 if sections["Contact Information"] else 0

    # Projects
    project_score = 10 if sections["Projects"] else 0

    # Experience
    experience_score = 10 if sections["Experience"] else 0

    score = (
        skill_score
        + min(section_score, 25)
        + length_score
        + contact_score
        + project_score
        + experience_score
    )

    return min(score, 100)


# -----------------------------
# Generate Suggestions
# -----------------------------
def generate_suggestions(text, skills, sections):

    suggestions = []

    if not sections["Contact Information"]:
        suggestions.append(
            "Add your email address and phone number."
        )

    if not sections["Summary / Objective"]:
        suggestions.append(
            "Add a professional summary or career objective."
        )

    if not sections["Education"]:
        suggestions.append(
            "Add an Education section."
        )

    if not sections["Experience"]:
        suggestions.append(
            "Add your work experience or internship experience."
        )

    if not sections["Skills"]:
        suggestions.append(
            "Add a clearly labelled Skills section."
        )

    if not sections["Projects"]:
        suggestions.append(
            "Add relevant academic or personal projects."
        )

    if not sections["Certifications"]:
        suggestions.append(
            "Add relevant certifications if you have them."
        )

    if len(skills) < 5:
        suggestions.append(
            "Add more relevant technical skills based on the job you are applying for."
        )

    word_count = len(text.split())

    if word_count < 250:
        suggestions.append(
            "Your resume appears short. Add relevant projects, achievements, skills, or experience."
        )

    if word_count > 1000:
        suggestions.append(
            "Your resume may be too long. Try to keep the content concise and relevant."
        )

    if not suggestions:
        suggestions.append(
            "Your resume has a good structure. Keep improving it with measurable achievements and job-specific keywords."
        )

    return suggestions


# -----------------------------
# User Interface
# -----------------------------
st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and get an ATS-style analysis of your "
    "skills, sections, resume score, and improvement suggestions."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


if uploaded_file:

    with st.spinner("Analyzing your resume..."):

        resume_text = extract_resume_text(uploaded_file)

        if not resume_text.strip():

            st.error(
                "Could not extract text from this resume. "
                "Please upload a text-based PDF or DOCX file."
            )

        else:

            # Find skills
            skills = find_skills(resume_text)

            # Check sections
            sections = check_sections(resume_text)

            # Calculate score
            score = calculate_score(
                resume_text,
                skills,
                sections
            )

            # Generate suggestions
            suggestions = generate_suggestions(
                resume_text,
                skills,
                sections
            )

            # -----------------------------
            # Results
            # -----------------------------
            st.success("Resume analyzed successfully!")

            st.subheader("📊 Resume Score")

            st.progress(score / 100)

            if score >= 80:
                st.success(f"Excellent Resume — {score}/100")

            elif score >= 60:
                st.warning(f"Good Resume — {score}/100")

            else:
                st.error(f"Needs Improvement — {score}/100")

            # -----------------------------
            # Statistics
            # -----------------------------
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Words",
                    len(resume_text.split())
                )

            with col2:
                st.metric(
                    "Skills Found",
                    len(skills)
                )

            with col3:
                st.metric(
                    "Sections Found",
                    sum(sections.values())
                )

            st.divider()

            # -----------------------------
            # Skills
            # -----------------------------
            st.subheader("🛠️ Skills Detected")

            if skills:

                skill_text = " • ".join(skills)

                st.info(skill_text)

            else:

                st.warning(
                    "No recognized skills were detected."
                )

            # -----------------------------
            # Resume Sections
            # -----------------------------
            st.subheader("📋 Resume Sections")

            for section, found in sections.items():

                if found:
                    st.success(
                        f"✓ {section}"
                    )

                else:
                    st.error(
                        f"✗ {section}"
                    )

            # -----------------------------
            # Suggestions
            # -----------------------------
            st.subheader("💡 Suggestions")

            for suggestion in suggestions:

                st.write(
                    f"• {suggestion}"
                )

            # -----------------------------
            # Resume Preview
            # -----------------------------
            st.subheader("📄 Resume Text Preview")

            with st.expander("View extracted resume text"):

                st.text(resume_text)
