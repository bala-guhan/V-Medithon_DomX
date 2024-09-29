import google.generativeai as genai
import os
from docx import Document
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

st.title("Med-Report (Interactive)")
# Set the API key
api_key = "AIzaSyDwrLsUBYvq78CrymNFLMthcWqhz2FJdIo"
os.environ['GEMINI_API_KEY'] = api_key  # Use the correct variable for the API key

# Configure the API with the correct environment variable
genai.configure(api_key=os.environ["GEMINI_API_KEY"])  # Changed from "API_KEY" to "GEMINI_API_KEY"

# Create an instance of the GenerativeModel
model = genai.GenerativeModel("gemini-1.5-flash")
doctor_remark = """Dictation for Medical Report:

"Patient's name is Vignaraja Sundar, a 21-year-old male, presenting today with a history of ADHD and symptoms associated with malnutrition. The patient reports difficulty concentrating, hyperactivity, and forgetfulness, which have been ongoing for several years. He also mentions fatigue, muscle weakness, and occasional dizziness, likely related to inadequate nutritional intake.

Upon examination, the patient appears underweight with a BMI of 18.3, suggesting mild undernutrition. There are signs of possible vitamin deficiencies, including brittle nails and dry skin. Blood pressure is within normal limits, though slightly on the lower end (110/70 mmHg).

Lab work has been ordered, including a full blood count, vitamin levels (especially B12, D, and iron), and a metabolic panel to assess overall health. We are particularly concerned about iron deficiency anemia and possible B12 deficiency contributing to his cognitive and physical symptoms.

For ADHD, the patient has not been previously treated with medication. I recommend starting with a low dose of methylphenidate, titrating upwards as needed based on symptom control and tolerability. Cognitive behavioral therapy (CBT) and dietary adjustments, particularly increasing protein and omega-3 intake, should also be part of the treatment plan.

For the malnutrition, I am recommending a high-protein diet with supplementation of multivitamins, particularly B12, D3, and iron. The patient should follow up with a nutritionist to develop a sustainable meal plan. We will recheck lab results in one month and adjust the treatment accordingly.

In summary, the patient is diagnosed with attention-deficit/hyperactivity disorder (ADHD) and malnutrition, both of which will be managed through medication, dietary adjustments, and behavioral interventions."

"""

def func(content = doctor_remark):
# Generate content using the model
    response = model.generate_content(f""""Write a medial report based on the remarks given by doctor : {content}. Based on this provide a detailed medical report on a fromat like Patient Identification: Name, Date of Birth, ID Number
    Medical History: Past and Present Conditions
    Medication and Allergies: Current Regimen and Reactions
    Family History: Relevant Hereditary Conditions
    Examination Findings: Vital Signs, Observed Symptoms
    Diagnostic Tests: X-Rays, Blood Tests, etc.
    Treatment Documentation: Medications and Procedures
    """)
    return response.text


def get_plot(csv_file = 'blood_test_report.csv'):
    # Convert the CSV string into a DataFrame
    blood_test_df = pd.read_csv(csv_file)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.barh(blood_test_df['Test'], blood_test_df['Value'], color='skyblue')

    # Adding a horizontal line for the normal range for each test
    for index, row in blood_test_df.iterrows():
        normal_range = row['Normal Range']
        if normal_range != '<200':
            low, high = map(float, normal_range.split('-'))
            plt.hlines(y=index, xmin=low, xmax=high, color='green', linewidth=2, label='Normal Range' if index == 0 else "")

    # Labels and Title
    plt.xlabel('Value')
    plt.title('Blood Test Results')
    plt.legend()
    plt.grid(axis='x')
    plt.savefig('blood_test_results.jpg', format='jpg', dpi=300, bbox_inches='tight')
    return 'blood_test_results.jpg'
    # plt.show()

