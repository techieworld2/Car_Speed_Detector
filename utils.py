
import cv2
import os

def create_output_dirs():
    os.makedirs("output/passed", exist_ok=True)
    os.makedirs("output/failed", exist_ok=True)

def draw_detection_line(frame, y_pos):
    cv2.line(frame, (0, y_pos), (frame.shape[1], y_pos), (0, 255, 255), 2)

def draw_measurement_line(frame, cx, cy, line_y):
    if abs(cy - line_y) <= 100:
        cv2.line(frame, (cx, cy), (cx, line_y), (255, 0, 255), 2)

def save_cropped_car_image(frame, x1, y1, x2, y2, track_id, status):
    crop = frame[y1:y2, x1:x2]
    if crop.size > 0:
        folder = "failed" if "Failed" in status else "passed"
        path = f"output/{folder}/car_{track_id}.jpg"
        cv2.imwrite(path, crop)
