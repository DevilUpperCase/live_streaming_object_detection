# Object Detection for Live Streaming

This repository demonstrates a Python script that performs object detection on live streams using [YOLOv8](https://github.com/ultralytics/ultralytics) and dynamically generates a GIF from the last 5 seconds of the stream.

## Example Output

Below is a sample GIF created by the script, demonstrating YOLOv8's object detection capabilities:

![Sample Output](last_5_seconds.gif)


## Features

- **YOLOv8 Object Detection**: Utilizes the YOLOv8 model for real-time object detection.
- **Dynamic Frame Capture**: Captures the last 5 seconds of a live stream for processing.
- **GIF Creation**: Converts the processed frames into a GIF for easy visualization.

## How It Works

1. **Live Stream Access**:
   - The script retrieves a live stream from YouTube using `yt-dlp` to extract the video stream URL.
2. **Object Detection**:
   - YOLOv8 is used to annotate frames in real time.
3. **GIF Generation**:
   - Frames from the last 5 seconds are stitched together into a GIF.

## Requirements

- Python 3.7+
- Libraries: `ultralytics`, `opencv-python`, `moviepy`, `yt-dlp`

Install the dependencies with:
```bash
pip install ultralytics opencv-python moviepy yt-dlp
```

## Usage

Run the script by specifying the YouTube live stream URL:
```bash
python yolo_streaming_to_gif.py
```

Once the script completes, the output GIF will be saved as `last_5_seconds.gif`.

## How to Customize

- **Model**: Change the YOLO model by modifying the line `model = YOLO('yolov8m.pt')`.
- **Capture Duration**: Adjust `capture_duration` to capture a longer or shorter segment of the stream.
- **FPS**: Customize the FPS for the GIF by changing the `fps` value during GIF creation.

## Troubleshooting

- **Error: Could not retrieve video stream URL**:
   Ensure the YouTube URL is correct and that `yt-dlp` is installed.
- **Error: Failed to read frame**:
   The video stream may have stopped or the URL might be invalid.
- **No frames processed**:
   Verify the live stream URL and ensure the video format is supported.
