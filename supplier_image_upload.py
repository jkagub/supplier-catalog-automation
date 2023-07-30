#!/usr/bin/env python3

import requests
import os

# Set the input directory where images are located
input_directory = "supplier-data/images"

# Set the URL of the endpoint where images will be uploaded
url = "http://localhost/upload/"

def upload_images():
    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file has a .jpeg extension
        if filename.endswith(".jpeg"):
            # Get the full path of the image
            image_path = os.path.join(input_directory, filename)
            # Open the image file in binary read mode
            with open(image_path, "rb") as file:
                # Use the requests library to POST the image file to the specified URL
                response = requests.post(url, files={"file": file})
                # Check the response status code to ensure successful upload
                if response.status_code == 201:
                    print(f"Image {filename} uploaded successfully.")
                else:
                    print(f"Error uploading image {filename}. Status code: {response.status_code}")

if __name__ == "__main__":
    # Call the upload_images function to start the image upload process
    upload_images()