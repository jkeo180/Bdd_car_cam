from pathlib import Path

# === CONFIGURATION FILE FOR BDD100K TO YOLO FORMAT CONVERSION ===

# Path to the BDD100K images directory containing train/val/test folders with .jpg images
IMAGES_ROOT = Path(r"C:\Users\11\bdd_car_cam\train")

# Path to the BDD100K labels directory containing the JSON files (train/val/test.json)
LABELS_ROOT = Path(r"C:\Users\11\bdd_car_cam\train")

# Destination folder where YOLO-formatted dataset will be saved
OUTPUT_DATASET_DIR = Path(r"C:\Users\11\bdd_car_cam\bdd100k-to-yolo\yolo_labels")

# Flag: Set to True to generate dataset in Ultralytics YOLO format (YOLOv7+)
# Set to False to generate legacy YOLO format
USE_ULTRALYTICS_FORMAT = True