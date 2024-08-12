from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder='output_images', image_format='png'):
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Create the output folder if it doesn't exist
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Save each image to the output folder
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.{image_format}')
        image.save(image_path, image_format.upper())
        print(f'Saved {image_path}')
    
    return images

# Example usage
pdf_path = 'test.pdf'
convert_pdf_to_images(pdf_path)
