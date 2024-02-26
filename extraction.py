import os
import PyPDF2
import spacy
from collections import defaultdict

# Load the spaCy model for English (optional, based on your needs for additional text processing)



# Define the occupations and their corresponding skills (for matching purposes)
occupations = {
    "Software Developer": ["Python", "Java"],
    "Project Manager": ["Project Management", "Communication"],
    "Data Scientist": ["Python", "Machine Learning"]
}

# Initialize ExtractSkills with a toy taxonomy configuration file
from ojd_daps_skills.pipeline.extract_skills.extract_skills import ExtractSkills #import the module

es = ExtractSkills(config_name="extract_skills_toy", local=True) #instantiate with toy taxonomy configuration file

es.load() #load necessary models

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # Ensure there's text on the page
                text += page_text + " "
    return text



def extract_skills_from_text(text, es):
    """Identifies skills in the text using ojd_daps_skills."""
    job_adverts = ["Software Development graduate from the University of Liverpool with 3+ years experience working in a team to deliver high-end solutions using recent tools and technologies. Possess excellent teamwork skills and a keen eye for design with full appreciation for building clean and user-friendly applications, and delivering cutting edge solutions."]  # Wrap the text in a list as expected by the extract_skills method
    job_skills_matched = es.extract_skills(job_adverts)  # Extract skills
    found_skills = set()  # Use a set to avoid duplicates
    for skill in job_skills_matched:
        # Assuming job_skills_matched returns a list of dictionaries with skill details
        found_skills.add(skill['skill_name'])  # Adjust based on actual output structure
    return list(found_skills)

def match_skills_to_occupations(found_skills, occupations):
    """Matches found skills to potential occupations."""
    matched_occupations = defaultdict(list)
    for occupation, required_skills in occupations.items():
        for skill in found_skills:
            if skill in required_skills:
                matched_occupations[occupation].append(skill)
    return dict(matched_occupations)

def process_single_resume(pdf_path, es, occupations):
    """Processes a single PDF resume."""
    text = extract_text_from_pdf(pdf_path)  # Use pdf_path as an argument
    found_skills = extract_skills_from_text(text, es)  # Extract skills using ojd_daps_skills
    matched_occupations = match_skills_to_occupations(found_skills, occupations)

    result = {
        "Resume": os.path.basename(pdf_path),
        "Found Skills": found_skills,
        "Matched Occupations": matched_occupations
    }

    return result

# Example usage with a specific PDF path
pdf_path = "Uploaded_Resumes/CV(2024).pdf"  # Adjust the path as necessary
result = process_single_resume(pdf_path, es, occupations)
print(f"Resume: {result['Resume']}")
print(f"Found Skills: {result['Found Skills']}")
print(f"Matched Occupations: {result['Matched Occupations']}\n")
