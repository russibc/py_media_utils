"""
This script downloads audio from a YouTube video (including Shorts) using pytube,
converts it to MP3 format with moviepy, and saves the output file using a sanitized
version of the video title. Temporary files are removed after conversion, and console
messages indicate progress or errors.
"""

import os
import re
from pytube import YouTube
from moviepy import AudioFileClip

# Hardcoded YouTube video URL
video_url = "https://www.youtube.com/shorts/example"

# Normalize Shorts URL to standard YouTube format
match = re.search(r"shorts/([a-zA-Z0-9_-]+)", video_url)
if match:
    video_id = match.group(1)
    normalized_url = f"https://www.youtube.com/watch?v={video_id}"
else:
    normalized_url = video_url

# Download audio stream
yt = YouTube(normalized_url)
stream = yt.streams.get_audio_only()
print(f"Downloading: {yt.title}")
downloaded_file = stream.download(filename="temp_audio.mp4")

# Sanitize filename for output
mp3_filename = re.sub(r'[\\/*?:"<>|]', "", yt.title.replace(" ", "_")) + ".mp3"

# Convert to MP3
audio_clip = AudioFileClip(downloaded_file)
audio_clip.write_audiofile(mp3_filename)
audio_clip.close()

# Remove temporary file
os.remove(downloaded_file)
print(f"Converted to MP3: {mp3_filename}")