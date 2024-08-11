

import openai
import json
from docx2pdf import convert
from pdf2image import convert_from_path
import os
import subprocess

# Set up OpenAI API key
with open('openaikey.txt', 'r') as file:
    # Read the contents of the file
    text = file.read()

# Print the contents of the file
print(text)
openai.api_key = text
# def process_images_with_openai(images_folder):
#     clauses = []

#     # Loop through all image files in the folder
#     for image_file in sorted(os.listdir(images_folder)):
#         if image_file.endswith('.png'):
#             image_path = os.path.join(images_folder, image_file)
            
#             # Read the image
#             with open(image_path, 'rb') as image:
#                 image_data = image.read()

#             # Send the image to OpenAI's vision API
#             response = openai.Image.create(image=image_data, purpose="document-analysis")

#             # Process the response (this depends on the API's exact response format)
#             # Assuming the API can return the clause titles and contents in a structured format
#             clauses.extend(response.get("clauses", []))
    
#     return {"clauses": clauses}



def convert_docx_to_pdf(docx_path, output_pdf_path):
    # Use LibreOffice in headless mode to convert .docx to .pdf
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', docx_path, '--outdir', os.path.dirname(output_pdf_path)])
    return output_pdf_path

def convert_pdf_to_images(pdf_path, output_folder='output_images', image_format='png'):
    from pdf2image import convert_from_path
    # Convert PDF to images
    print('2'+pdf_path)
    images = convert_from_path(pdf_path)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Save each image to the output folder
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.{image_format}')
        image.save(image_path, image_format.upper())
        print(f'Saved {image_path}')
    
    return images

def convert_docx_to_images(docx_path, output_folder='output_images', image_format='png'):
    # Convert .docx to .pdf using LibreOffice
    output_pdf_path = os.path.join(output_folder, 'Commercial_Letter_of_Intent_to_Lease.pdf')
    print('\n\n1'+output_pdf_path+'\n\n')
    convert_docx_to_pdf(docx_path, output_pdf_path)
    
    # Convert .pdf to images
    images = convert_pdf_to_images(output_pdf_path, output_folder, image_format)
    
    return images

# Example usage
docx_path = 'Commercial_Letter_of_Intent_to_Lease.docx'
convert_docx_to_images(docx_path)


def process_images_with_gpt4_vision(images_folder):
    clauses = []

    # Loop through all image files in the folder
    for image_file in sorted(os.listdir(images_folder)):
        if image_file.endswith('.png'):
            image_path = os.path.join(images_folder, image_file)
            
            # Read the image
            with open(image_path, 'rb') as image:
                image_data = image.read()

            # Send the image to GPT-4 Vision (or another OpenAI model that supports image inputs)
            response = openai.Image.create(
                image=image_data,
                prompt= "This is a leasing agreement. Usinng the json format ",
                purpose="document-analysis"
            )

            # Process the response (this depends on the API's exact response format)
            # Assuming the API can return the clause titles and contents in a structured format
            clauses.extend(response.get("clauses", []))
    
    return {"clauses": clauses}

# Example usage
images_folder = 'output_images'  # Folder containing the .png files
result = process_images_with_gpt4_vision(images_folder)

# Save the result to a JSON file
output_json_path = 'output_clauses.json'
with open(output_json_path, 'w') as json_file:
    json.dump(result, json_file, indent=2)

print(f"Output saved to {output_json_path}")