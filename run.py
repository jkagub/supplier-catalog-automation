#!/usr/bin/env python3

import os
import requests

# Set the input directory where text files (descriptions) are located
input_directory = "supplier-data/descriptions"

# Set the URL of the endpoint where fruit data will be uploaded
url = "http://localhost/fruits/"

def process_and_upload():
    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file has a .txt extension (text file)
        if filename.endswith(".txt"):
            # Open the text file in read mode
            with open(os.path.join(input_directory, filename), "r") as file:
                # Read all lines from the file into a list
                lines = file.readlines()
                # Extract data from the file and create a dictionary with fruit data
                fruit_data = {
                    "name": lines[0].strip(),  # Get the first line as the name (remove leading/trailing spaces)
                    "weight": int(lines[1].strip().split()[0]),  # Get the weight from the second line (convert to integer)
                    "description": lines[2].strip(),  # Get the third line as the description (remove leading/trailing spaces)
                    "image_name": os.path.splitext(filename)[0] + ".jpeg"  # Generate the image name from the file name
                }
                # Use the requests library to POST the fruit data to the specified URL
                response = requests.post(url, json=fruit_data)
                # Check the response status code to ensure successful upload
                if response.status_code == 201:
                    print(f"Fruit data from {filename} uploaded successfully.")
                else:
                    print(f"Error uploading fruit data from {filename}. Status code: {response.status_code}")

if __name__ == "__main__":
    # Call the process_and_upload function to start processing and uploading fruit data
    process_and_upload()
