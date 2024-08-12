# Commercial_Letter_of_Intent_to_Lease.docx

import os
from docx2pdf import convert
from pdf2image import convert_from_path

def convert_docx_to_pdf(docx_path, output_pdf_path):
    convert(docx_path, output_pdf_path)

def convert_pdf_to_images(pdf_path, output_folder='output_images', image_format='png'):
    # Convert PDF to images
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
    # Step 1: Convert .docx to .pdf
    output_pdf_path = os.path.join(output_folder, 'output.pdf')
    convert_docx_to_pdf(docx_path, output_pdf_path)
    
    # Step 2: Convert .pdf to images
    images = convert_pdf_to_images(output_pdf_path, output_folder, image_format)
    
    return images

# Example usage
docx_path = 'Commercial_Letter_of_Intent_to_Lease.docx'
convert_docx_to_images(docx_path)
