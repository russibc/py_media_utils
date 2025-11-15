"""
This script compresses a PDF file using Ghostscript by applying different
quality settings (screen, ebook, printer, prepress) until the output file
size is less than or equal to a specified maximum size. It checks if the
input file exists, attempts compression with each quality setting, and
prints the results. Console messages indicate success or failure.
"""

import subprocess
import os

# Input and output PDF file names
input_pdf = "input.pdf"
output_pdf = "output_compressed.pdf"

# Maximum allowed size in bytes
max_size_bytes = 2_000_000

# Check if the input file exists
if not os.path.exists(input_pdf):
    raise FileNotFoundError(f"File not found: {input_pdf}")

# Possible quality settings: screen < ebook < printer < prepress
qualities = ["screen", "ebook", "printer", "prepress"]

compression_successful = False

for quality in qualities:
    try:
        subprocess.run([
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{quality}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_pdf}",
            input_pdf
        ], check=True)

        size = os.path.getsize(output_pdf)
        print(f"Quality: {quality} → Size: {size} bytes")

        if size <= max_size_bytes:
            print(f"Success: PDF compressed to {size} bytes.")
            compression_successful = True
            break
    except subprocess.CalledProcessError as error:
        print(f"Error using Ghostscript: {error}")
        break

if not compression_successful:
    print(f"Failure: No compression achieved the desired size ({max_size_bytes} bytes).")