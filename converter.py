import json
import os
from pathlib import Path

# --- CONFIGURATION ---
json_dir = Path(r"C:\Users\11\bdd_car_cam\train\ann")
output_dir = Path(r"C:\Users\11\bdd_car_cam\bdd100k-to-yolo\yolo_labels\labels\train")
output_dir.mkdir(parents=True, exist_ok=True)

# BDD100K Standard Classes
classes = ["person", "rider", "car", "bus", "truck", "bike", "motor", "traffic light", "traffic sign", "train"]

def convert_to_yolo():
    for json_file in json_dir.glob("*.json"):
        with open(json_file, 'r') as f:
            data = json.load(f)
            
            # Use original filename without .json for the .txt label
            txt_filename = json_file.stem.replace(".jpg", "") + ".txt"
            with open(output_dir / txt_filename, 'w') as out_f:
                # BDD100K individual JSONs often have a 'frames' or 'labels' list
                labels = data.get('labels', [])
                for label in labels:
                    if 'box2d' not in label or label['category'] not in classes:
                        continue
                    
                    cls_id = classes.index(label['category'])
                    box = label['box2d']
                    
                    # BDD100K coordinates: x1, y1, x2, y2 (absolute pixels)
                    # YOLO needs: center_x, center_y, width, height (normalized 0-1)
                    # BDD100K standard resolution is 1280x720
                    dw = 1.0 / 1280
                    dh = 1.0 / 720
                    
                    x = (box['x1'] + box['x2']) / 2.0
                    y = (box['y1'] + box['y2']) / 2.0
                    w = box['x2'] - box['x1']
                    h = box['y2'] - box['y1']
                    
                    out_f.write(f"{cls_id} {x*dw:.6f} {y*dh:.6f} {w*dw:.6f} {h*dh:.6f}\n")
    print(f"Done! YOLO labels saved to: {output_dir}")

if __name__ == "__main__":
    convert_to_yolo()

