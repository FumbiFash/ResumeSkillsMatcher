# ResumeSkillsMatcher
Match skills to occupations


This Python script is designed to extract skills from PDF resumes and match them to predefined occupations based on required skills. It leverages PyPDF2 for reading PDF files, spaCy for optional text processing, and the ojd_daps_skills library for skill extraction.

Getting Started

Before running the script, ensure you have Python installed on your system and that you've installed the required dependencies.

Dependencies
PyPDF2: For extracting text from PDF files.
spaCy: Optional, for additional text processing.
ojd_daps_skills: For extracting skills from text using a pre-defined taxonomy.

You can install these dependencies using pip:

pip install PyPDF2 spacy ojd_daps_skills

If you plan to use spaCy for additional text processing, you'll also need to download a spaCy language model. For English, you can install it like this:
python -m spacy download en_core_web_sm

Configuration
Before running the script, you need to define the occupations and their corresponding skills in the occupations dictionary within the script

Usage

The script contains functions to process a single PDF resume:

extract_text_from_pdf(pdf_path): Extracts text from a specified PDF file.
extract_skills_from_text(text, es): Identifies skills in the extracted text.
match_skills_to_occupations(found_skills, occupations): Matches identified skills to the predefined occupations.
process_single_resume(pdf_path, es, occupations): Orchestrates the process of extracting text, identifying skills, and matching them to occupations.
To use the script, ensure you have a PDF resume file ready, and adjust the pdf_path variable accordingly. Then, run the script to see the extracted skills and matched occupations.


Customization

Modify the occupations dictionary to include other occupations and their required skills as needed.
Adjust the spaCy model or implement additional text processing as needed for your specific use case.
Customize the ExtractSkills instantiation if you have a different taxonomy configuration.


