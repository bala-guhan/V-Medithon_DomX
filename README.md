<div>
  <br />
# V-Medithon_DomX
**V-Medithon_DomX** is an interactive web-based medical diagnosis report generator designed to automate the process of generating patient reports. It simplifies data input, approval, and visual representation of lab results for healthcare providers.
    </a>
  <br />

  <div>
    <img src="https://img.shields.io/badge/-Next_JS-black?style=for-the-badge&logoColor=white&logo=nextdotjs&color=000000" alt="nextdotjs" />
    <img src="https://img.shields.io/badge/-TypeScript-black?style=for-the-badge&logoColor=white&logo=typescript&color=3178C6" alt="typescript" />
    <img src="https://img.shields.io/badge/-Tailwind_CSS-black?style=for-the-badge&logoColor=white&logo=tailwindcss&color=06B6D4" alt="tailwindcss" />
    <img src="https://img.shields.io/badge/-Appwrite-black?style=for-the-badge&logoColor=white&logo=appwrite&color=FD366E" alt="appwrite" />
  </div>

## Features

- **Automated Report Generation**: Pulls patient data from JSON files and generates medical reports.
- **Graphical Representation**: Automatically plots lab results with normal ranges.
- **User Interaction**: Users can approve or rectify personal and diagnosis data.
- **Medication Data Handling**: Loads medication data for the final report.

## Requirements

- Python 3.9 or above
- Libraries: `streamlit`, `pandas`, `matplotlib`, `json`, `os`, `time`, `docx`
- `Streamlit` (optional for alternate UI interface)

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bala-guhan/V-Medithon_DomX.git
   cd V-Medithon_DomX

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the app
   ```bash
   streamlit run app.py
