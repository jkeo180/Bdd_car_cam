# BDD100K to YOLO Converter

![Development Status](https://img.shields.io/badge/status-stable-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.9%2B-purple)
![YOLO](https://img.shields.io/badge/YOLOv3--v11-compatible-green)
![Open Source](https://img.shields.io/badge/Contributions-Welcome-orange)

A lightweight Python tool to convert the [BDD100K dataset](http://bdd-data.berkeley.edu/) into **YOLO format**, supporting:
- Ultralytics YOLOv7/v11 directory structure
- Legacy YOLO structure
- YOLO `.txt` label generation with normalized `x_center y_center width height`
- `.yaml`, `.names`, and `.data` config file generation
- Dataset verification utility for both formats

**Read the walkthrough on Medium**: [From BDD100K to YOLO](https://medium.com/@kavin.aravindhan/bdd100k-to-yolo-conversion-9c331a7dc9f3)  

## Project Structure

```text
bdd100k-to-yolo/
│
├── config.py              # Set dataset paths and format toggle
├── converter.py           # Main script to convert BDD100K to YOLO
├── verify_dataset.py      # Script to check image-label consistency
├── requirements.txt       # Minimal dependencies
├── LICENSE                # MIT License
├── README.md              # You're reading it!
└── .gitignore
````

## Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/KavinAravindhan/bdd100k-to-yolo.git
cd bdd100k-to-yolo
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Configure paths

Edit `config.py` and set:

```python
IMAGES_ROOT = Path("/path/to/bdd100k/100k_images")
LABELS_ROOT = Path("/path/to/bdd100k/100k_labels")
OUTPUT_DATASET_DIR = Path("./dataset_yolo_converted")
USE_ULTRALYTICS_FORMAT = True  # or False for legacy format
```

### 4. Run the converter

```bash
python3 converter.py
```

## Folder Structures

### Ultralytics Format (USE_ULTRALYTICS_FORMAT = True)

```text
dataset_yolo_converted/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
├── bdd100k_ultralytics.yaml
└── yolo_files/
    ├── train.txt
    ├── val.txt
    ├── test.txt
    ├── bdd100k.names
    └── bdd100k.data
```

### Legacy Format (USE_ULTRALYTICS_FORMAT = False)

```text
dataset_yolo_converted/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
└── yolo_files/
    ├── train.txt
    ├── val.txt
    ├── test.txt
    ├── bdd100k.names
    └── bdd100k.data
```

## Verify Dataset Consistency

Ensure all image-label pairs are present using:

### For Ultralytics format:

```bash
python verify_dataset.py --dataset ./dataset_yolo_converted
```

### For Legacy format:

```bash
python verify_dataset.py --dataset ./dataset_yolo_converted --legacy
```

## 🤝 Contributing

Contributions are welcome!
If you find any bugs or have ideas to improve this tool, feel free to:

* Open an issue
* Fork this repository
* Create a pull request

Let’s make this tool better, together!

## Tested With

* Python 3.9–3.12
* BDD100K official dataset
* Ultralytics YOLOv7/v11
* YOLO Darknet format

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⭐️ If you find this useful...

Give this repo a ⭐️ on GitHub and share it with others working with BDD100K or YOLO!
