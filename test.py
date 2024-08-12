
from openai import OpenAI
import json
from docx2pdf import convert
from pdf2image import convert_from_path
import os
import subprocess
from helper import encode_image, create_request

# client = OpenAI()

def convert_docx_to_pdf(docx_path, output_pdf_path):
    # Use LibreOffice in headless mode to convert .docx to .pdf
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', docx_path, '--outdir', os.path.dirname(output_pdf_path)])
    return output_pdf_path

def convert_pdf_to_images(pdf_path, output_folder='output_images', image_format='png'):
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
    # Initialize a list to hold the image files
    base64_images = []

    # Loop through all image files in the folder
    for image_file in sorted(os.listdir(images_folder)):
        if image_file.endswith('.png'):
            image_path = os.path.join(images_folder, image_file)
            base64_images += [encode_image(image_path)]
    response_json = create_request(base64_images)
    
    return response_json

# Example usage
images_folder = 'output_images'  # Folder containing the .png files
result = process_images_with_gpt4_vision(images_folder)



# Step 1: Remove the markdown formatting (```json ... ```)
if result.startswith("```json"):
    result = result[7:].strip()
if result.endswith("```"):
    result = result[:-3].strip()

# Step 2: Handle potentially incomplete content
# If the JSON is cut off, you'll need to detect this and handle it.
try:
    parsed_result = json.loads(result)
except json.JSONDecodeError:
    print("The JSON content appears to be incomplete or invalid.")
    # You can handle the incomplete content here, maybe log it or retry the request.
    exit(1)

# Step 3: Save the parsed dictionary to a JSON file
output_json_path = 'output_clauses.json'
with open(output_json_path, 'w') as json_file:
    json.dump(parsed_result, json_file, indent=2)

print(f"Output saved to {output_json_path}")

# # Save the result to a JSON file
# output_json_path = 'output_clauses.json'
# with open(output_json_path, 'w') as json_file:
#     json.dump(result, json_file, indent=2)

# print(f"Output saved to {output_json_path}")