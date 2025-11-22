"""
This script converts an OGG audio file to MP3 format using the pydub library.
It checks if the input file exists, defines the output path if not specified,
and exports the converted audio as an MP3 file. Console messages indicate
success or errors during the process.
"""

import os
from pydub import AudioSegment

# Input OGG file path
ogg_path = "example.ogg"

# Define output MP3 file path
mp3_path = os.path.splitext(ogg_path)[0] + ".mp3"

# Check if the input file exists
if not os.path.isfile(ogg_path):
    raise FileNotFoundError(f"File not found: {ogg_path}")

# Load the OGG file
audio = AudioSegment.from_ogg(ogg_path)

# Export as MP3
audio.export(mp3_path, format="mp3")

print(f"File successfully converted: {mp3_path}")