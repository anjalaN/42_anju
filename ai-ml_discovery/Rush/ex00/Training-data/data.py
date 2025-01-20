#!/usr/bin/env python3
from matplotlib import pyplot
from matplotlib.image import imread
import os
'''
#!/usr/bin/env python3
from matplotlib import pyplot
from matplotlib.image import imread
import os

folder = '/home/arajapak/ai-ml_discovery/Rush/ex00/Training-data/Dog'  # Absolute path

print("Loading images from:", os.path.abspath(folder))
print("Files in Dog folder:", os.listdir(folder))


for i in range(9):
    filename = os.path.join(folder, 'Dog' + str(i) + '.jpg')  # Correct file path concatenation
    try:
        image = imread(filename)
        pyplot.subplot(330 + 1 + i)
        pyplot.imshow(image)
    except FileNotFoundError:
        print(f"File {filename} not found.")
pyplot.show()
#########################################3
#!/usr/bin/env python3
from matplotlib import pyplot
from matplotlib.image import imread
import os

# Correct path to the 'Dog' folder inside 'Training-data'
folder = '/home/arajapak/ai-ml_discovery/Rush/ex00/Training-data/Dog/'

# Get and sort the filenames in the 'Dog' folder
image_files = sorted([f for f in os.listdir(folder) if f.startswith('Dog') and f.endswith('.jpg')])

print("Sorted files:", image_files)  # Debugging line

# Display the first 9 images
for i in range(min(9, len(image_files))):  # Ensure we don't go beyond the available files
    filename = os.path.join(folder, image_files[i])
    print(f"Looking for file: {filename}")  # Debugging line
    try:
        image = imread(filename)
        pyplot.subplot(330 + 1 + i)
        pyplot.imshow(image)
    except FileNotFoundError:
        print(f"File {filename} not found.")
pyplot.show()

##########################################
'''
#!/usr/bin/env python3
from matplotlib import pyplot
from matplotlib.image import imread
import os

# Correct path to the 'Dog' folder inside 'Training-data'
folder = '/home/arajapak/ai-ml_discovery/Rush/ex00/Training-data/Dog/'

# Get and sort the filenames in the 'Dog' folder
image_files = sorted([f for f in os.listdir(folder) if f.startswith('Dog') and f.endswith('.jpg')])

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




#!/usr/bin/env python3
from matplotlib import pyplot
from matplotlib.image import imread
import os
import cv2  # OpenCV for resizing images
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Correct path to the 'Dog' folder inside 'Training-data'
folder = '/home/arajapak/ai-ml_discovery/Rush/ex00/Training-data/Dog/'

# Get and sort the filenames in the 'Dog' folder
image_files = sorted([f for f in os.listdir(folder) if f.startswith('Dog') and f.endswith('.jpg')])

print("Sorted files:", image_files)  # Debugging line

# Parameters for resizing
img_size = (128, 128)  # Resize all images to 128x128

# Max number of images to display (e.g., display up to Dog30.jpg)
max_images_to_show = 30

# You can use a list to store images and labels if you're building a dataset
images = []
labels = []

# Ensure we don't go beyond the available files and that the images exist
for i in range(min(max_images_to_show, len(image_files))):  # Load up to 'max_images_to_show'
    filename = os.path.join(folder, image_files[i])
    print(f"Looking for file: {filename}")  # Debugging line
    try:
        # Load image using OpenCV for resizing
        image = imread(filename)

        # Resize image to 128x128
        image_resized = cv2.resize(image, img_size)

        # Normalize image (scaling pixel values to range [0, 1])
        image_normalized = image_resized / 255.0  # Normalize to [0, 1]

        # Optional: Here you can encode labels if you have different classes. 
        # Assuming you have labels based on file name, e.g., 'Dog0.jpg' -> label '0'
        label = int(image_files[i].split('Dog')[1].split('.jpg')[0])  # Extracting label from file name

        # Append image and label
        images.append(image_normalized)
        labels.append(label)

        # Adjust the subplot grid dynamically based on the number of images
        pyplot.subplot(6, 5, i + 1)  # Arrange in a 6x5 grid (up to 30 images)
        pyplot.imshow(image_normalized)
        pyplot.axis('off')  # Turn off axis for better image visualization

    except FileNotFoundError:
        print(f"File {filename} not found.")

pyplot.show()

# Convert images and labels into numpy arrays (useful for model training)
images = np.array(images)
labels = np.array(labels)

# Optionally: Encode labels if they are categorical (use LabelEncoder)
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

print("Encoded Labels:", encoded_labels)
