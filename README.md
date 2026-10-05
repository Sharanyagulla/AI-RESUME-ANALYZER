# 📄 AI Resume Analyzer

AI Resume Analyzer is a Python-based web application that analyzes a resume and provides an ATS-style resume score, detected skills, section analysis, and suggestions for improvement.

The application is built using **Python and Streamlit**.

## 🚀 Features

* Upload resume in **PDF** or **DOCX** format
* Extract text from the uploaded resume
* Detect technical and soft skills
* Check important resume sections
* Generate an ATS-style resume score
* Display resume word count
* Provide improvement suggestions
* Preview extracted resume text
* Simple and user-friendly web interface

## 🛠️ Technologies Used

* Python
* Streamlit
* PyPDF2
* python-docx

## 📁 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI_Resume_Analyzer.git
```

### 2. Open the project folder

```bash
cd AI_Resume_Analyzer
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your web browser.

## 📄 How to Use

1. Open the application.
2. Click **Upload your Resume**.
3. Select a PDF or DOCX resume.
4. The application extracts the resume text.
5. Skills and important sections are detected.
6. An ATS-style score is generated.
7. Suggestions are displayed to improve the resume.

## 📊 Resume Analysis

The application checks:

* Contact Information
* Summary / Objective
* Education
* Experience
* Skills
* Projects
* Certifications
* Resume length
* Technical and soft skills

## 📈 Resume Score

The application generates a score from **0 to 100** based on:

* Skills found
* Resume sections
* Resume length
* Contact information
* Projects
* Experience

The score is intended as a basic ATS-style indicator and should not be considered an actual score from a specific company's ATS.

## 🔮 Future Enhancements

The project can be improved by adding:

* AI-powered resume analysis using an LLM
* Job description matching
* Missing keyword detection
* Skill gap analysis
* Resume recommendations
* Resume ranking
* PDF report generation
* User login and authentication
* Database connectivity
* Resume improvement suggestions using AI

## 🎯 Project Objective

The main objective of this project is to help students and job seekers quickly analyze their resumes and identify areas that can be improved before applying for jobs.

## 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/your-username`

## 📜 License

This project is created for educational and learning purposes.

```
```
