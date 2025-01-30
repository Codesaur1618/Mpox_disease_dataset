import os
import hashlib
from PIL import Image

# Function to compute the hash of an image
def compute_image_hash(image_path):
    try:
        # Open the image using Pillow
        with Image.open(image_path) as img:
            # Convert image to a consistent mode and size
            img = img.convert("RGB")
            img = img.resize((8, 8))  # Resize to a smaller size to speed up comparison

            # Convert image to bytes
            img_bytes = img.tobytes()

            # Use hashlib to generate an MD5 hash of the image
            return hashlib.md5(img_bytes).hexdigest()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

# Function to find and delete duplicates in a folder
def find_and_delete_duplicates(folder_path):
    # Dictionary to store hashes and filenames
    hashes = {}
    duplicate_count = 0
    deleted_files = []

    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out directories (only keep files)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Iterate over each file and check for duplicates
    for file in files:
        file_path = os.path.join(folder_path, file)

        # Compute the hash for the current image
        file_hash = compute_image_hash(file_path)
        
        if file_hash:
            if file_hash in hashes:
                # If the hash is already in the dictionary, it's a duplicate
                print(f"Duplicate found: {file_path}")
                try:
                    # Delete the duplicate image
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    duplicate_count += 1
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            else:
                # Otherwise, store the file path with its hash
                hashes[file_hash] = file_path

    return deleted_files, duplicate_count

# Path to the folder containing the images
folder_path = 'F:/Monkeypox reserach/Resized_dataset'

# Find duplicates and delete them
deleted_files, duplicate_count = find_and_delete_duplicates(folder_path)

# Output the result
print(f"Found and deleted {duplicate_count} duplicate images.")
for deleted_file in deleted_files:
    print(f"Deleted: {deleted_file}")
