"""
This script converts a .WEBM video file to .MP4 format and trims it to a
specified time range using ffmpeg. It checks if the input file exists,
applies recommended encoding settings for broad compatibility, and saves
the output video in the current directory. Console messages indicate
success or errors during the process.
"""

import subprocess
import os

# Input and output file names
input_webm = "input.webm"
output_mp4 = "output.mp4"

# Start and end times (format: "HH:MM:SS" or in seconds)
start_time = "00:00:27"
end_time = "00:04:58"

# Check if the input file exists
if not os.path.exists(input_webm):
    raise FileNotFoundError(f"File not found: {input_webm}")

# ffmpeg command to convert and trim
command = [
    "ffmpeg",
    "-y",  # overwrite output file without asking
    "-i", input_webm,
    "-ss", start_time,
    "-to", end_time,
    "-c:v", "libx264",  # video codec
    "-pix_fmt", "yuv420p",  # wide compatibility with players
    output_mp4
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print(f"Conversion and trimming completed: {output_mp4}")
except subprocess.CalledProcessError as error:
    print(f"Error executing ffmpeg: {error}")