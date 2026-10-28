import json
import os
import pathlib
import pandas as pd
import numpy as np
import opencv as opencv
import kagglehub as kagglehub
from kagglehub import kaggleDatasetAdapter
import matplotlib.pyplot as plt
import labelimg as labling
import zipfile
import os

data = json.load(file) 
os.makedirs('labels', exist_ok=True) 
for img in data:
    name = img['name'] - Get width / height → w = img['width']; h = img['height'] - Make a label file → label_path = flabels/{name.split('.')[0]}.txt - Open that file to write → f = open(label_path, 'w') - Then loop over labels → for label in img['labels']: - If label['category'] is a class you care about (car, person, etc.): - box = label['box2d'] - center_x = (box['x1'] + box['x2']) / 2 / w - center_y = (box['y1'] + box['y2']) / 2 / h - width = (box['x2'] - box['x1']) / w - height = (box['y2'] - box['y1']) / h - class_id = your_class_map[label['category'] # like {'car': 2, 'person': 0} - write: f.write(f{class_id} {center_x:.6f} {center_y:.6f} {width:.6f} {height:.6f}\n) - Close the file → f.close()
    w = img['width']
    h = img['height']
    label_path = f'labels/{name.split(".")[0]}.txt'
    f = open(label_path, 'w')
    for label in img['labels']:
        if label['category'] in your_class_map:
            box = label['box2d']
            center_x = (box['x1'] + box['x2']) / 2 / w
            center_y = (box['y1'] + box['y2']) / 2 / h
            width = (box['x2'] - box['x1']) / w
            height = (box['y2'] - box['y1']) / h
            class_id = your_class_map[label['category']]
            f.write(f"{class_id} {center_x:.6f} {center_y:.6f} {width:.6f} {height:.6f}\n")
    f.close()['name']
    w = img['width']