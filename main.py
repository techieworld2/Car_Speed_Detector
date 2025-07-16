
from utils import create_output_dirs
from detector import run_speed_detection

if __name__ == "__main__":
    print("Initializing directories and model: ")
    create_output_dirs()
    run_speed_detection()
    print("Processing complete. Check the output folder.")
