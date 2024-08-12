import os
import subprocess

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
