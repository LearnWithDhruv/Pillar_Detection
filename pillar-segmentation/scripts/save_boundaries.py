import json
import os
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import INPUT_DIR, OUTPUT_DIR
from detect_pillars import detect_pillars

def save_boundaries_to_json(pillars, output_file):
    boundaries = {f"pillar_{i + 1}": [point[0].tolist() for point in pillar] for i, pillar in enumerate(pillars)}

    with open(output_file, "w") as json_file:
        json.dump(boundaries, json_file, indent=4)

if __name__ == "__main__":
    for file_name in os.listdir(OUTPUT_DIR):
        if file_name.startswith("preprocessed_") and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            preprocessed_image_path = os.path.join(OUTPUT_DIR, file_name)

            pillars = detect_pillars(preprocessed_image_path)
            output_file = os.path.join(OUTPUT_DIR, f"{file_name.replace('preprocessed_', '').split('.')[0]}_boundaries.json")
            save_boundaries_to_json(pillars, output_file)
            print(f"Saved boundaries: {output_file}")
