import os
from PIL import Image

# Function to resize images to 416x416
def resize_image(image_path, new_path, new_size=(416, 416)):
    try:
        with Image.open(image_path) as img:
            # Resize the image
            img_resized = img.resize(new_size)
            # Save the resized image to the new path
            img_resized.save(new_path)
            print(f"Resized and saved image: {new_path}")
    except Exception as e:
        print(f"Error resizing {image_path}: {e}")

# Path to the folder containing the images
folder_path = 'F:/Monkeypox reserach/Scraped images/normal new set'

# Path to the output folder where resized images will be saved
output_folder = 'F:/Monkeypox reserach/Resized_dataset_new'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all files in the folder
files = os.listdir(folder_path)

# Filter out directories (optional, if you want only files)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Sort the files (optional, based on the name or modification date)
files.sort()

# Iterate through the files to rename them and resize images
for index, file in enumerate(files, start=1):
    # Get the file extension
    file_extension = os.path.splitext(file)[1].lower()
    
    # Only process image files (you can add more extensions if needed)
    if file_extension in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
        # Create a new file name with the index
        new_name = f"file_{index}{file_extension}"
        
        # Get the full paths for the old and new names
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(output_folder, new_name)
        
        # Check if the file already exists in the new location
        if os.path.exists(new_path):
            print(f"Skipping {file}: {new_name} already exists in the output folder.")
            continue
        
        # Resize the image and save it in the new folder
        resize_image(old_path, new_path, new_size=(416, 416))
        
    else:
        print(f"Skipping non-image file: {file}")
