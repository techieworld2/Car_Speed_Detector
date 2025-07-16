import cv2
from ultralytics import YOLO
from collections import defaultdict
from config import *
from utils import *

def run_speed_detection():
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(INPUT_VIDEO)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    line_y = int(height * 0.6)

    out = cv2.VideoWriter(OUTPUT_VIDEO, cv2.VideoWriter_fourcc(*'XVID'), fps, FRAME_SIZE)

    object_tracks = defaultdict(list)
    car_status = {}
    saved_image_flags = {}

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, FRAME_SIZE)
        results = model.track(frame, persist=True, conf=CONFIDENCE_THRESHOLD)[0]

        draw_detection_line(frame, line_y)

        if results.boxes.id is not None:
            for box, track_id in zip(results.boxes.xyxy, results.boxes.id):
                x1, y1, x2, y2 = map(int, box.tolist())
                cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
                draw_measurement_line(frame, cx, cy, line_y)

                track_id = int(track_id.item())
                object_tracks[track_id].append((cx, cy))

                if track_id not in car_status and abs(cy - line_y) <= LINE_PROXIMITY:
                    if len(object_tracks[track_id]) >= 2:
                        (px1, py1), (px2, py2) = object_tracks[track_id][-2], object_tracks[track_id][-1]
                        pixel_distance = ((px2 - px1) ** 2 + (py2 - py1) ** 2) ** 0.5
                        speed_mps = (pixel_distance / PIXELS_PER_METER) * fps
                        speed_kmph = speed_mps * MPS_TO_KMPH

                        result = f"{'Failed' if speed_kmph > SPEED_LIMIT else 'Passed'}: {int(speed_kmph)} km/h"
                        car_status[track_id] = result

                        if track_id not in saved_image_flags:
                            save_cropped_car_image(frame, x1, y1, x2, y2, track_id, result)
                            saved_image_flags[track_id] = True

                # Draw labels and boxes
                label = car_status.get(track_id, "car")
                color = (0, 255, 0) if "Passed" in label else (0, 0, 255) if "Failed" in label else (255, 255, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Show total counts
        passed = sum(1 for v in car_status.values() if "Passed" in v)
        failed = sum(1 for v in car_status.values() if "Failed" in v)

        cv2.putText(frame, f"Passed: {passed}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(frame, f"Failed: {failed}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        out.write(frame)
        cv2.imshow("Speed Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
