import os

# Path to the folder containing the files
folder_path = "F:/Monkeypox reserach/Scraped images/normal new set"

# List all files in the folder
files = os.listdir(folder_path)

# Filter out directories (optional, if you want only files)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Sort the files (optional, based on the name or modification date)
files.sort()

# Iterate through the files and rename them
for index, file in enumerate(files, start=1):
    # Get the file extension
    file_extension = os.path.splitext(file)[1]
    
    # Create a new file name with the index
    new_name = f"img_{index}{file_extension}"
    
    # Get the full paths for the old and new names
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)
    
    print(f"Renamed: {file} -> {new_name}")
