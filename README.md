
# Pillar Segmentation Project

## Overview
This project is designed to detect pillars or columns in an image, segment them, and assign unique colors to each pillar. It also extracts and stores the boundaries of each pillar as a set of points in a JSON file.

## Directory Structure
```
pillar-segmentation-project/
├── data/                 # For storing input and output images
│   ├── input/            # Input images go here
│   ├── output/           # Processed images and JSON output
├── scripts/              # Main Python scripts
│   ├── preprocess.py     # For preprocessing input images
│   ├── detect_pillars.py # Main logic for pillar detection
│   ├── visualize.py      # For visualization and coloring
│   ├── save_boundaries.py# For dumping boundary points into JSON
├── config.py             # Configuration settings
├── requirements.txt      # Required Python packages
└── README.md             # Project overview and usage instructions
```

## Prerequisites
- Python 3.7 or higher
- Required Python libraries listed in `requirements.txt`

## Installation
1. Clone the repository or download the project files.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Modify the `config.py` file for project settings such as:
- Directory paths for input and output.
- Parameters for preprocessing, like Canny edge detection thresholds.

Example `config.py`:
```python
# Directory paths
INPUT_DIR = './data/input/'
OUTPUT_DIR = './data/output/'

# Parameters for preprocessing
CANNY_THRESHOLDS = (50, 150)
```

## Usage
Follow these steps to run the project:

### 1. Preprocess Images
Convert input images to grayscale, apply noise reduction, and thresholding.
```bash
python scripts/preprocess.py
```
- Input: Images in `data/input/`
- Output: Preprocessed images in `data/output/`

### 2. Detect Pillars
Detect and segment pillars from the preprocessed images.
```bash
python scripts/detect_pillars.py
```
- Input: Preprocessed images in `data/output/`
- Output: List of detected pillars printed to the console.

### 3. Visualize Pillars
Overlay colored masks on the original image to visualize the detected pillars.
```bash
python scripts/visualize.py
```
- Input: Original and preprocessed images in `data/`
- Output: Visualized images saved in `data/output/`

### 4. Save Boundaries
Save pillar boundaries as a JSON file for each image.
```bash
python scripts/save_boundaries.py
```
- Input: Preprocessed images in `data/output/`
- Output: JSON files with boundary points in `data/output/`

### Example Output
#### Visualized Image
- Pillars are highlighted with unique colors.
#### JSON File
Boundary points stored in the format:
```json
{
  "pillar_1": [[x1, y1], [x2, y2], ...],
  "pillar_2": [[x1, y1], [x2, y2], ...]
}
```

## Dependencies
Listed in `requirements.txt`:
```
opencv-python
numpy
```

## Notes
- The project supports `.png`, `.jpg`, and `.jpeg` image formats.
- Ensure that input images are placed in the `data/input/` directory before running the scripts.

## Future Enhancements
- Support for more complex pillar shapes.
- Integration of a machine learning model for better accuracy.
- Web interface for uploading and visualizing results.

## License
This project is licensed under the MIT License.
