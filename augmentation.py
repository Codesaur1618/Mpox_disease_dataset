import cv2
import numpy as np
import os

def apply_augmentations(input_folder, output_base_folder):
    # Create folders for each augmentation type
    augmentation_types = ["original", "greyscale", "negative", "sharpen", "hsv"]
    for aug_type in augmentation_types:
        os.makedirs(os.path.join(output_base_folder, aug_type), exist_ok=True)

    # Loop through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load the image
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            # Original filename (without extension) to use in augmented images
            name, ext = os.path.splitext(filename)
            
            # Save the original image
            cv2.imwrite(os.path.join(output_base_folder, "original", filename), img)
            
            # Greyscale
            grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(output_base_folder, "greyscale", f"{name}_greyscale{ext}"), grey_img)
            
            # Negative Transformation
            negative_img = cv2.bitwise_not(img)
            cv2.imwrite(os.path.join(output_base_folder, "negative", f"{name}_negative{ext}"), negative_img)
            
            # Sharpening
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            sharpened_img = cv2.filter2D(img, -1, kernel)
            cv2.imwrite(os.path.join(output_base_folder, "sharpen", f"{name}_sharpen{ext}"), sharpened_img)
            
            # HSV Adjustment (Increasing Saturation)
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_img)
            s = cv2.add(s, 50)  # Increase saturation by 50
            s = np.clip(s, 0, 255)
            hsv_adjusted_img = cv2.merge([h, s, v])
            hsv_adjusted_img = cv2.cvtColor(hsv_adjusted_img, cv2.COLOR_HSV2BGR)
            cv2.imwrite(os.path.join(output_base_folder, "hsv", f"{name}_hsv{ext}"), hsv_adjusted_img)

# Paths to your input folder and base output folder
input_folder = "F:/Monkeypox reserach/Resized_dataset_new"
output_base_folder = "F:/Monkeypox reserach/Augmented_img"

# Apply augmentations and organize output
apply_augmentations(input_folder, output_base_folder)
