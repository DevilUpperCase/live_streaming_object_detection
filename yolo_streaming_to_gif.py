import subprocess
import cv2
from ultralytics import YOLO
from moviepy.editor import ImageSequenceClip

# Load the YOLO model
model = YOLO('yolov8m.pt')

# YouTube live stream URL
youtube_url = 'https://youtu.be/80MaYh4ksQk'

# Get video stream URL
command = ["yt-dlp", "-f", "best", "-g", youtube_url]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
video_stream_url = result.stdout.strip()

if not video_stream_url:
    print("Error: Could not retrieve video stream URL.")
    exit()

print(f"Video stream URL: {video_stream_url}")

# Open the video stream
cap = cv2.VideoCapture(video_stream_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Get frame rate
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0  # Default to 30 FPS if unavailable
print(f"FPS: {fps}")

# Capture the last 5 seconds dynamically
capture_duration = 5  # seconds
frames_to_capture = int(fps * capture_duration)
frames = []
current_frames = 0

while current_frames < frames_to_capture:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame.")
        break

    try:
        results = model(frame)
        annotated_frame = results[0].plot()
        frames.append(annotated_frame)
        current_frames += 1
        print(f"Processed frame: {current_frames}/{frames_to_capture}")
    except Exception as e:
        print(f"Error during YOLO inference: {e}")
        break

cap.release()

if not frames:
    print("No frames processed. Exiting.")
    exit()

# Create a GIF
clip = ImageSequenceClip(frames, fps=fps)
clip.write_gif('last_5_seconds.gif', fps=fps)

print("GIF saved to last_5_seconds.gif")
