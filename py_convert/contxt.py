import docx

def replace_disease_type_in_template(txt_file_path, template_path, output_path):
    try:
        # Read disease type from the text file
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            disease_type = f.read().strip()  # Read and strip any extra whitespace/newlines
        
        # Open the Word template
        doc = docx.Document(template_path)

        # Iterate over the paragraphs and replace the {disease_type} placeholder
        for paragraph in doc.paragraphs:
            if '{disease_type}' in paragraph.text:
                print(f"Replacing '{disease_type}' in paragraph: {paragraph.text}")  # Debugging output
                paragraph.text = paragraph.text.replace('{disease_type}', disease_type)

        # Save the updated document
        doc.save(output_path)
        print(f"Updated template generated successfully: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
txt_file_path = r'C:\Users\isher\OneDrive\Desktop\py covert\disease_type.txt'  # Path to your txt file
template_path = r'C:\Users\isher\OneDrive\Desktop\py covert\Output_file.docx'  # Path to your Word template
output_path = r'C:\Users\isher\OneDrive\Desktop\py covert\Output_file.docx'  # Path to save the updated Word document

# Call the function to replace the disease type in the Word template
replace_disease_type_in_template(txt_file_path, template_path, output_path)
