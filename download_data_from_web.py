import fiftyone as fo
import os
import requests
import zipfile
import io

# Download the zip file
url = "https://github.com/thesteve0/fiftyone-getting-started/releases/download/v.data/downloads.zip"
response = requests.get(url, stream=True)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))

# Extract the zip file to a directory
extract_dir = "downloads"
os.makedirs(extract_dir, exist_ok=True)
zip_file.extractall(extract_dir)

# Create a FiftyOne dataset from the extracted images
dataset = fo.Dataset.from_dir(
    dataset_dir=extract_dir,
    dataset_type=fo.types.ImageDirectory,
    name="downloaded-dataset"
)

# Launch the FiftyOne App
session = fo.launch_app(dataset)
session.wait()