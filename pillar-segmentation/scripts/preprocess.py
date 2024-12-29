import cv2
import os
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import INPUT_DIR, OUTPUT_DIR

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    adaptive_thresh = cv2.adaptiveThreshold(
        gray_image, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 
        11, 2
    )
    
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    _, thresholded_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)

    return thresholded_image


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for file_name in os.listdir(INPUT_DIR):
        file_path = os.path.join(INPUT_DIR, file_name)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            preprocessed_image = preprocess_image(file_path)
            output_path = os.path.join(OUTPUT_DIR, f"preprocessed_{file_name}")
            cv2.imwrite(output_path, preprocessed_image)
            print(f"Saved preprocessed image: {output_path}")
