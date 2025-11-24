"""
This script downloads audio from a YouTube video (including Shorts) using yt-dlp
and converts it to MP3 format. The output file is saved with the video title as
its filename. Error handling is included to catch issues during the download or
conversion process.
"""

import subprocess

# Hardcoded YouTube video URL
video_url = "https://www.youtube.com/shorts/example"

print("Downloading and converting to MP3...")

try:
    subprocess.run([
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--output", "%(title)s.%(ext)s",
        video_url
    ], check=True)
    print("Download and conversion completed successfully!")
except subprocess.CalledProcessError as error:
    print(f"Error executing yt-dlp: {error}")