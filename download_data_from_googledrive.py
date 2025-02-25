import os
import requests
import zipfile
import io
import gdown
import fiftyone as fo

# Google Drive file ID
file_id = "1e3EqCNJStVMkb_jhJwhl3PQq_7_RuIQN"

# Download the zip file from Google Drive
url = f"https://drive.google.com/uc?id={file_id}"
download_dir = "downloads/jaguars"
os.makedirs(download_dir, exist_ok=True)
output = os.path.join(download_dir, "test1.zip")
try:
    gdown.download(url, output, quiet=False)
except Exception as e:
    print(f"Error downloading file: {e}")
    print("Please ensure the file is shared publicly on Google Drive and that gdown is installed.")
    exit()

# Extract the zip file to a directory
# Inside downloads/jaguars there will a directory for each jaguar
# containing images of the jaguar
extract_dir = "downloads/jaguars"
os.makedirs(extract_dir, exist_ok=True)
try:
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
except FileNotFoundError:
    print(f"Error: The file {output} was not found. Check if the download was successful.")
    exit()

