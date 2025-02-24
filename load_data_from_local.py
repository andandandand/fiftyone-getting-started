import fiftyone as fo
import os

# Be sure to mount the data volume before running this script
# Uncomment the line inside the devcontainer.json file and replace with 
# the path to the directory containing the images in your local machine 
#   "mounts": [
#      "source=/Users/antonio/Documents/Projects/kaggle-dogs-vs-cats/train,target=/data/train,type=bind,consistency=cached"
#   ],

# Path to the directory containing the images
images_dir = "/data/train"

# Create a FiftyOne dataset
dataset = fo.Dataset("dogs-vs-cats")

# Get a list of image paths
image_paths = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith((".png", ".jpg", ".jpeg"))]

# Create FiftyOne samples, one for each image
samples = [fo.Sample(filepath=image_path) for image_path in image_paths]

# Add samples to the dataset
dataset.add_samples(samples)

# Launch the FiftyOne App
session = fo.launch_app(dataset)
session.wait()