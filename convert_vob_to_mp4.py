"""
This script converts all .VOB video files in the current directory into .MP4 format
using ffmpeg. The converted files are saved in a subdirectory named 'converted'.
It preserves video quality, applies recommended encoding settings, and displays
the conversion time for each video as well as the total duration.
"""

#!/usr/bin/env python3
import os
import subprocess
import time

# Define source and destination directories
source_directory = os.getcwd()
destination_directory = os.path.join(source_directory, "converted")
os.makedirs(destination_directory, exist_ok=True)

# Find all .VOB files in the current directory
vob_files = [file for file in os.listdir(source_directory) if file.lower().endswith(".vob")]

if not vob_files:
    print("No .VOB files found in the current directory.")
else:
    total_start = time.time()

    for file in vob_files:
        input_path = os.path.join(source_directory, file)
        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(destination_directory, f"{base_name}.mp4")

        command = [
            "ffmpeg",
            "-i", input_path,
            "-c:v", "libx264",
            "-crf", "18",
            "-preset", "slow",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            output_path
        ]

        print(f"\nConverting: {file} → {base_name}.mp4")
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
    print(f"\nConversion completed for {len(vob_files)} files in {total_duration:.2f} seconds.")