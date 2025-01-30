import os
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

# Directory containing the original images
original_dir = "F:/Monkeypox reserach/final dataset/original_data/negative"
# Directory containing the enhanced images
enhanced_dir = 'F:/Monkeypox reserach/final dataset/Final_data/negative_enhanced'

# List of image filenames (ensure both directories have the same files)
image_filenames = [f for f in os.listdir(original_dir) if f.endswith(('.jpg', '.png'))]

# Initialize lists to store PSNR and SSIM values
psnr_values = []
ssim_values = []

for filename in image_filenames:
    # Construct full file paths
    original_path = os.path.join(original_dir, filename)
    enhanced_path = os.path.join(enhanced_dir, filename)

    # Open images
    original_image = Image.open(original_path).convert('RGB')
    enhanced_image = Image.open(enhanced_path).convert('RGB')

    # Convert images to numpy arrays
    original_array = np.array(original_image)
    enhanced_array = np.array(enhanced_image)

    # Ensure images are at least 7x7 pixels
    if original_array.shape[0] < 7 or original_array.shape[1] < 7:
        print(f"Skipping {filename} due to insufficient size.")
        continue

    # Calculate PSNR
    psnr_value = psnr(original_array, enhanced_array)
    psnr_values.append(psnr_value)

    # Calculate SSIM
    ssim_value = ssim(original_array, enhanced_array, multichannel=True)
    ssim_values.append(ssim_value)

# Calculate average PSNR and SSIM
avg_psnr = np.mean(psnr_values)
avg_ssim = np.mean(ssim_values)

print(f'Average PSNR: {avg_psnr}')
print(f'Average SSIM: {avg_ssim}')