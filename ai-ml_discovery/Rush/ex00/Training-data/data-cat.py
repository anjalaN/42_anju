#!/usr/bin/env python3
from matplotlib import pyplot
from matplotlib.image import imread
import os

# Correct path to the 'Dog' folder inside 'Training-data'
folder = '/home/arajapak/ai-ml_discovery/Rush/ex00/Training-data/Cat/'

# Get and sort the filenames in the 'Dog' folder
image_files = sorted([f for f in os.listdir(folder) if f.startswith('Cat') and f.endswith('.jpg')])

print("Sorted files:", image_files)  # Debugging line

# Display images from Dog0.jpg to Dog50.jpg
max_images_to_show = 30  # Max number of images to display (up to Dog50.jpg)

# Ensure we don't go beyond the available files and that the images exist
for i in range(min(max_images_to_show, len(image_files))):  # Load up to 50 images
    filename = os.path.join(folder, image_files[i])
    print(f"Looking for file: {filename}")  # Debugging line
    try:
        image = imread(filename)
        # Adjust the subplot grid dynamically based on the number of images
        pyplot.subplot(10, 5, i + 1)  # Arrange in a 10x5 grid (max 50 images)
        pyplot.imshow(image)
    except FileNotFoundError:
        print(f"File {filename} not found.")

pyplot.show()


