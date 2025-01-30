import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time

# URL of the page to scrape
url = "https://dermnetnz.org/images/mpox-images"

# Folder to save images
output_folder = "dermnet_monkeypox_images"
os.makedirs(output_folder, exist_ok=True)

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags with the class 'js-gallery-image'
image_tags = soup.find_all('img', class_='js-gallery-image')

# Loop through each image tag
for i, img in enumerate(image_tags):
    # Get the 'src' attribute, which contains the image URL
    img_src = img.get('src')
    
    if img_src:
        # Create a full URL by joining the base URL with the image path
        img_url = urljoin(url, img_src)
        
        # Try to determine the correct file extension from the URL
        img_extension = img_url.split('.')[-1]
        valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']
        
        if img_extension.lower() in valid_extensions:
            try:
                # Download the image
                img_data = requests.get(img_url).content
                
                # Create a safe filename with an appropriate extension
                img_filename = os.path.join(output_folder, f"monkeypox_{i+1}.{img_extension}")
                
                # Save the image to the folder
                with open(img_filename, 'wb') as file:
                    file.write(img_data)
                    print(f"Downloaded {img_filename}")
                
                # Optional: delay between downloads to avoid rate limiting
                time.sleep(1)  # sleep for 1 second
            except Exception as e:
                print(f"Failed to download {img_url}: {e}")
        else:
            print(f"Skipping invalid image extension: {img_extension}")
