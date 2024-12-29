import cv2
import os
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import INPUT_DIR, OUTPUT_DIR

def detect_pillars(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    edges = cv2.Canny(image, 30, 100)  

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    pillars = []
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        pillars.append(approx)

    return pillars


if __name__ == "__main__":
    for file_name in os.listdir(OUTPUT_DIR):
        if file_name.startswith("preprocessed_") and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(OUTPUT_DIR, file_name)
            pillars = detect_pillars(image_path)
            print(f"Detected {len(pillars)} pillars in {file_name}")
