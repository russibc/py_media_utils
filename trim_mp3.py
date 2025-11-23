"""
This script trims a segment from an MP3 audio file using the pydub library.
It converts start and end times provided in the format hh:mm:ss:ms into
milliseconds, extracts the specified portion of the audio, and saves it
as a new MP3 file. Console messages indicate success or errors.
"""

import re
from pydub import AudioSegment
import os

# Input and output MP3 file names
input_mp3 = "input.mp3"
output_mp3 = "output_trimmed.mp3"

# Start and end times in the format hh:mm:ss:ms
start_time_str = "00:00:02:000"
end_time_str = "00:00:10:000"

# Convert time string to milliseconds
match_start = re.match(r"(\d+):(\d+):(\d+):(\d+)", start_time_str)
match_end = re.match(r"(\d+):(\d+):(\d+):(\d+)", end_time_str)

if not match_start or not match_end:
    raise ValueError("Invalid time format. Use hh:mm:ss:ms")

hours, minutes, seconds, milliseconds = map(int, match_start.groups())
start_time_ms = (hours * 3600 + minutes * 60 + seconds) * 1000 + milliseconds

hours, minutes, seconds, milliseconds = map(int, match_end.groups())
end_time_ms = (hours * 3600 + minutes * 60 + seconds) * 1000 + milliseconds

# Load the MP3 file
if not os.path.isfile(input_mp3):
    raise FileNotFoundError(f"File not found: {input_mp3}")

audio = AudioSegment.from_mp3(input_mp3)

# Trim the audio
trimmed_audio = audio[start_time_ms:end_time_ms]

# Export the trimmed segment
trimmed_audio.export(output_mp3, format="mp3")
print(f"Trimmed audio successfully exported to: {output_mp3}")