"""
This script removes a specified range of pages from a PDF file located in the same
directory as the script. The output file is saved with the original filename plus
'-removed' appended before the extension. Page numbers are provided in a human-
readable format (starting at 1), but internally adjusted to Python's zero-based index.
"""
import os
from PyPDF2 import PdfReader, PdfWriter

# Get the directory where this script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Input PDF file (must be in the same directory as this script)
input_pdf_name = "example.pdf"
input_pdf_path = os.path.join(script_directory, input_pdf_name)

# Output PDF file: original name + "-removed"
base_name, extension = os.path.splitext(input_pdf_name)
output_pdf_name = f"{base_name}-removed{extension}"
output_pdf_path = os.path.join(script_directory, output_pdf_name)

# Range of pages to remove (example: remove pages 3 to 5)
# Index starts at 1 for human readability
remove_start_page = 2
remove_end_page = 19

# Adjust for zero-based index in Python
remove_start_index = remove_start_page - 1
remove_end_index = remove_end_page - 1

reader = PdfReader(input_pdf_path)
writer = PdfWriter()

for page_index in range(len(reader.pages)):
    if not (remove_start_index <= page_index <= remove_end_index):
        writer.add_page(reader.pages[page_index])

with open(output_pdf_path, "wb") as output_file:
    writer.write(output_file)

print(f"Pages from {remove_start_page} to {remove_end_page} successfully removed.")
print(f"Output saved as: {output_pdf_name}")