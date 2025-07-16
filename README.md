
# Car Speed Detector using YOLOv8

A Python-based vehicle speed detection system that uses **YOLOv8 object detection** to track vehicles in a video, calculate their speed, and classify them as **Passed** or **Failed** based on a speed threshold.

---

## Demo Output

- Draws a detection line on video.
- Tracks vehicles and calculates their speed using distance between frames.
- Classifies each vehicle as:
  - `Passed` (within speed limit)
  - `Failed` (over speed limit)
- Annotates video with:
  - Bounding boxes
  - Speed labels
  - Summary stats (Passed/Failed count)
- Saves cropped images of detected vehicles into:
  - `passed/`
  - `failed/`

---

## Tech Stack

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- Python 3.8+

---

## Project Structure

```bash
car_speed_detector/
│
├── input/                   # Input videos (e.g., cars.mp4)
│   └── cars.mp4
│
├── output/                  # Processed output video and results
│
├── passed/                 # Cropped images of vehicles within speed limit
├── failed/                 # Cropped images of vehicles over speed limit
│
├── yolov8n.pt              # Pre-trained YOLOv8 model
│
├── config.py               # Configuration settings
├── detector.py             # Core logic for detection and speed check
├── utils.py                # Utility functions (e.g., speed calculations)
└── main.py                 # Entry point for running the pipeline
```

---

## How It Works

1. Loads the video and detects cars frame-by-frame.
2. Tracks each vehicle using YOLOv8 object tracking.
3. Computes pixel displacement between frames.
4. Converts it into speed (km/h) using:

```python
speed = (pixel_distance / PIXELS_PER_METER) * FPS * 3.6
```

5. If speed > threshold → marked as "Failed", else "Passed".
6. Saves vehicle snapshot into `passed/` or `failed/` folders.

---

## How to Run

### 1. Install Requirements

```bash
pip install ultralytics opencv-python
```

### 2. Place Input Video

Put your `.mp4` file in the `input/` directory (e.g., `input/cars.mp4`).

### 3. Run the Detector

```bash
python main.py
```

### 4. View Output

- Annotated video: `output/output_speed_check.mp4`
- Image snapshots: `passed/`, `failed/`

---

## Configuration

Edit `config.py` to change:

- Speed limit (e.g., 30 or 40 km/h)
- Line position
- Distance calibration (PIXELS_PER_METER)

---

## Limitations

- Assumes a fixed camera angle.
- Speed is estimated using pixel displacement — **not GPS-accurate**.
- Requires calibration (e.g., pixels per meter) to match real-world scale.

---

## Credits

Built with:
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)

---


