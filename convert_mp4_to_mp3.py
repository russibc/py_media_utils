"""
This script converts all .MP4 video files in the current directory into .MP3 format
using ffmpeg. The converted files are saved in a subdirectory named 'converted'.
It extracts audio from the video files, applies recommended encoding settings,
and displays the conversion time for each file as well as the total duration.
"""

#!/usr/bin/env python3
import os
import subprocess
import time

# Define source and destination directories
source_directory = os.getcwd()
destination_directory = os.path.join(source_directory, "converted")
os.makedirs(destination_directory, exist_ok=True)

# Find all .MP4 files in the current directory
mp4_files = [file for file in os.listdir(source_directory) if file.lower().endswith(".mp4")]

if not mp4_files:
    print("No .MP4 files found in the current directory.")
else:
    total_start = time.time()

    for file in mp4_files:
        input_path = os.path.join(source_directory, file)
        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(destination_directory, f"{base_name}.mp3")

        # ffmpeg command to extract audio and convert to MP3
        command = [
            "ffmpeg",
            "-i", input_path,
            "-vn",              # disable video
            "-c:a", "libmp3lame",
            "-q:a", "2",        # quality setting (lower is better, 0–9)
            output_path
        ]

        print(f"\nConverting: {file} → {base_name}.mp3")
        start = time.time()
        try:
            subprocess.run(command, check=True)
            end = time.time()
            duration = end - start
            print(f"Success: {output_path} (Time: {duration:.2f} seconds)")
        except subprocess.CalledProcessError as error:
            print(f"Error converting {file}: {error}")

    total_end = time.time()
    total_duration = total_end - total_start
    print(f"\nConversion completed for {len(mp4_files)} files in {total_duration:.2f} seconds.")
