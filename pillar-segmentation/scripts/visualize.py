import cv2
import os
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import INPUT_DIR, OUTPUT_DIR
from detect_pillars import detect_pillars

def visualize_pillars(original_image_path, pillars):
    image = cv2.imread(original_image_path)

    for pillar in pillars:
        color = [random.randint(0, 255) for _ in range(3)]
        cv2.drawContours(image, [pillar], -1, color, 2)

    return image


if __name__ == "__main__":
    for file_name in os.listdir(OUTPUT_DIR):
        if file_name.startswith("preprocessed_") and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            original_file = file_name.replace("preprocessed_", "")
            original_image_path = os.path.join(INPUT_DIR, original_file)
            preprocessed_image_path = os.path.join(OUTPUT_DIR, file_name)

            pillars = detect_pillars(preprocessed_image_path)
            visualized_image = visualize_pillars(original_image_path, pillars)

            output_path = os.path.join(OUTPUT_DIR, f"visualized_{original_file}")
            cv2.imwrite(output_path, visualized_image)
            print(f"Saved visualized image: {output_path}")
