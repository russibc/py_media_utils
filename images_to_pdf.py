"""
This script converts all PNG, JPG, and JPEG images in the current directory
into a single PDF file. Images are sorted alphabetically, converted to RGB,
and combined into one PDF document. Console messages indicate progress or
errors during the process.
"""

import os
from PIL import Image

# Supported extensions
supported_extensions = (".png", ".jpg", ".jpeg")

# Output PDF file name
output_pdf = "images_output.pdf"

# List and sort image files in the current directory
image_files = sorted(
    file_name for file_name in os.listdir(".")
    if file_name.lower().endswith(supported_extensions)
)

if not image_files:
    print("No PNG/JPG/JPEG images found in the current directory.")
else:
    images = []
    for file_name in image_files:
        try:
            image = Image.open(file_name).convert("RGB")
            images.append(image)
            print(f"Added: {file_name}")
        except Exception as error:
            print(f"Error opening {file_name}: {error}")

    # Create the PDF from the first image and append the others
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF successfully created: {output_pdf}")