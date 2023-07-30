#!/usr/bin/env python3

from PIL import Image
import os

input_directory = "supplier-data/images"

def process_images():
    # Check if the input directory exists
    if not os.path.exists(input_directory):
        print(f"Error: The directory '{input_directory}' does not exist.")
        return

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Get the full path of the image
        image_path = os.path.join(input_directory, filename)
        # Use 'with' block to ensure the image file is properly closed
        try:
            with Image.open(image_path) as image:
                # Convert to RGB if necessary
                if image.mode in ('RGBA', 'LA', 'P'):
                    image = image.convert('RGB')
                # Resize the image to 600x400 pixels
                new_image = image.resize((600, 400))
        except:
            print(f"Error: {image_path} is not a valid image file")
            continue

        # Create a new filename with JPEG extension
        new_filename = os.path.splitext(filename)[0] + ".jpeg"
        # Get the full path for the new image
        new_image_path = os.path.join(input_directory, new_filename)
        # Use 'with' block to save the new image and handle any exceptions

        try:
            new_image.save(new_image_path, "JPEG")
            print(f"Image {filename} processed and saved as {new_filename}")
        except Exception as e:
            print(f"Error processing image {filename}: {str(e)}")
    

if __name__ == "__main__":
    process_images()
