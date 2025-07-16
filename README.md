# Car Speed Detector

A computer vision-based system that detects and measures vehicle speeds from video input using YOLOv8 object detection and tracking. The system can classify vehicles as "Passed" or "Failed" based on configurable speed limits and save cropped images of detected vehicles.

## Features

- **Real-time Vehicle Detection**: Uses YOLOv8 for accurate vehicle detection and tracking
- **Speed Measurement**: Calculates vehicle speeds by tracking movement across video frames
- **Speed Limit Enforcement**: Classifies vehicles as "Passed" or "Failed" based on speed threshold
- **Visual Feedback**: Displays real-time speed measurements, detection lines, and pass/fail counts
- **Image Capture**: Saves cropped images of vehicles to separate folders based on pass/fail status
- **Video Output**: Generates annotated output video with speed measurements and classifications

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics YOLOv8
- NumPy
- Additional dependencies (automatically installed with ultralytics)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/techieworld2/Car_Speed_Detector.git
cd Car_Speed_Detector
```

2. Install required dependencies:
```bash
pip install ultralytics opencv-python
```

3. Ensure you have the input video file in the `input/` directory (default: `cars.mp4`)

## Usage

### Basic Usage

1. Place your input video file in the `input/` folder (or update the path in `config.py`)
2. Run the speed detection:
```bash
python main.py
```

3. The system will:
   - Process the video and detect vehicles
   - Measure speeds and classify as passed/failed
   - Save cropped images to `output/passed/` and `output/failed/` folders
   - Generate an annotated output video at `output/output_speed_check.avi`

### Configuration

Edit `config.py` to customize the system behavior:

```python
# Speed detection parameters
LINE_PROXIMITY = 30        # Proximity to detection line for speed measurement
SPEED_LIMIT = 40          # Speed limit in km/h for pass/fail classification
PIXELS_PER_METER = 8      # Calibration factor for pixel-to-meter conversion
MPS_TO_KMPH = 3.6         # Conversion factor from m/s to km/h

# File paths
INPUT_VIDEO = "input/cars.mp4"                    # Input video path
OUTPUT_VIDEO = "output/output_speed_check.avi"    # Output video path
FRAME_SIZE = (640, 360)                           # Output frame dimensions

# Detection parameters
CONFIDENCE_THRESHOLD = 0.5  # YOLO detection confidence threshold
```

## File Structure

```
Car_Speed_Detector/
├── main.py              # Entry point - initializes and runs detection
├── detector.py          # Main detection logic with YOLO tracking
├── config.py           # Configuration parameters
├── utils.py            # Utility functions (drawing, saving images)
├── yolov8n.pt         # Pre-trained YOLOv8 model
├── input/             # Input video directory
│   └── cars.mp4       # Sample input video
└── output/            # Output directory (created automatically)
    ├── passed/        # Images of vehicles that passed speed limit
    ├── failed/        # Images of vehicles that exceeded speed limit
    └── output_speed_check.avi  # Annotated output video
```

## How It Works

1. **Vehicle Detection**: The system uses YOLOv8 to detect and track vehicles in each frame
2. **Speed Calculation**: Vehicle speeds are calculated by measuring the distance traveled between consecutive frames
3. **Detection Line**: A horizontal line is drawn across the video where speed measurements are taken
4. **Classification**: Vehicles are classified as "Passed" (green) or "Failed" (red) based on the speed limit
5. **Image Saving**: Cropped images of each vehicle are saved when they cross the detection line
6. **Real-time Display**: The system shows live counts and speed measurements during processing

## Output

### Video Output
- Annotated video with bounding boxes around detected vehicles
- Color-coded classifications (green for passed, red for failed)
- Real-time speed measurements displayed above each vehicle
- Pass/fail counters in the top-left corner
- Detection line visible across the frame

### Image Output
- `output/passed/`: Cropped images of vehicles that stayed within speed limit
- `output/failed/`: Cropped images of vehicles that exceeded speed limit
- Images are named as `car_{track_id}.jpg`

## Customization

### Adjusting Speed Measurement Accuracy
- Modify `PIXELS_PER_METER` in `config.py` based on your video's scale
- Calibrate by measuring a known distance in pixels and converting to meters

### Changing Detection Sensitivity
- Adjust `CONFIDENCE_THRESHOLD` to change YOLO detection sensitivity
- Lower values detect more objects but may include false positives

### Modifying Speed Limits
- Change `SPEED_LIMIT` in `config.py` to set your desired threshold
- Speeds are measured in km/h

## Troubleshooting

### Common Issues

1. **No vehicles detected**: Lower the `CONFIDENCE_THRESHOLD` value
2. **Inaccurate speeds**: Adjust the `PIXELS_PER_METER` calibration factor
3. **Video not found**: Check the `INPUT_VIDEO` path in `config.py`
4. **Memory issues**: Reduce `FRAME_SIZE` for lower resolution processing

### Dependencies Issues
If you encounter installation issues, try:
```bash
pip install --upgrade pip
pip install ultralytics opencv-python --no-cache-dir
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the repository for license details.

## Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for object detection
- OpenCV for computer vision operations