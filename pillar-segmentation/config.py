import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, 'data/input/')
OUTPUT_DIR = os.path.join(BASE_DIR, 'data/output/')

CANNY_THRESHOLDS = (50, 150)
