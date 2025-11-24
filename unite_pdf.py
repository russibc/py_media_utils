"""
This script merges all PDF files located in the same directory as the script
into a single PDF document. The resulting file is saved with the name
'merged_output.pdf' by default. The script automatically excludes the output
file itself from the merge process, sorts the input files alphabetically,
and provides console messages for each file added or if any errors occur.
"""
import os
from PyPDF2 import PdfMerger

# Get the directory where this script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the output PDF file name
output_file_name = "merged_output.pdf"

# List and sort PDF files in the current directory, excluding the output file
pdf_files = sorted(
    file_name for file_name in os.listdir(script_directory)
    if file_name.lower().endswith(".pdf") and file_name != output_file_name
)

if not pdf_files:
    print("No PDF files found in the current directory.")
else:
    merger = PdfMerger()

    for pdf_file in pdf_files:
        try:
            merger.append(os.path.join(script_directory, pdf_file))
            print(f"Added: {pdf_file}")
        except Exception as error:
            print(f"Error adding {pdf_file}: {error}")

    merger.write(os.path.join(script_directory, output_file_name))
    merger.close()
    print(f"PDFs successfully merged into: {output_file_name}")