import os
import requests
import zipfile
import io
import gdown
import fiftyone as fo

# Google Drive file ID
file_id = "1BlvnENeDjbkBOV_3AJbyLLgEZTwQX2f3"

# Download the zip file from Google Drive
url = f"https://drive.google.com/uc?id={file_id}"
download_dir = "downloads/test"
os.makedirs(download_dir, exist_ok=True)
output = os.path.join(download_dir, "test1.zip")
try:
    gdown.download(url, output, quiet=False)
except Exception as e:
    print(f"Error downloading file: {e}")
    print("Please ensure the file is shared publicly on Google Drive.")
    exit()

# Extract the zip file to a directory
extract_dir = "downloads/test_cats_vs_dogs"
os.makedirs(extract_dir, exist_ok=True)
try:
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
except FileNotFoundError:
    print(f"Error: The file {output} was not found. Check if the download was successful.")
    exit()

# Create a FiftyOne dataset from the extracted images
dataset = fo.Dataset.from_dir(
    dataset_dir=extract_dir,
    dataset_type=fo.types.ImageDirectory,
    name="downloaded-dataset"
)

# Launch the FiftyOne App
session = fo.launch_app(dataset)
session.wait()