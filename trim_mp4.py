"""
This script trims a video file using the moviepy library. It loads a video from
the current directory, cuts a segment based on specified start and end times
(in minutes and seconds), and saves the trimmed video as a new file. Console
messages indicate progress and the name of the output file.
"""

from moviepy import VideoFileClip
import os

# Input video file (must be in the same directory as this script)
video_filename = "input_video.mp4"

# Start and end times (minutes and seconds)
start_minute = 27
start_second = 43
end_minute = 33
end_second = 53

# Convert times to seconds
start_time = start_minute * 60 + start_second
end_time = end_minute * 60 + end_second

# Load the video
clip = VideoFileClip(video_filename)

# Trim the video
trimmed_clip = clip.subclipped(start_time, end_time)

# Output video file name
output_filename = "trimmed_video.mp4"

# Save the new video
trimmed_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")

print(f"Video successfully trimmed and saved as {output_filename}")