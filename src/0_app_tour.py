import fiftyone as fo
import fiftyone.zoo as foz
from pprint import pprint

# Load the quickstart dataset
# This is a small dataset that ships with fiftyone
# It contains a few images and labels
# It's a good starting point for learning the library

# This is a subset of 200 images from the COCO-2017 validation dataset
# When loading the dataset, we will get prediction from pre-trained Faster R-CNN model 
# from torchvision.models.detection
# This model is trained on the COCO-2017 dataset and is able to detect 80 classes of objects
dataset = foz.load_zoo_dataset("quickstart") 

session = fo.launch_app(dataset)

## Print available label fields in a nicely formatted way
#print("\nDataset Field Schema:")
#print("-------------------")
#for field_name, field_type in dataset.get_field_schema().items():
#    print(f"{field_name:<20} : {field_type.__class__.__name__}")

## Print a sample's predictions
# sample = dataset.first()
# print(sample["predictions"])  # Should show detections from Faster R-CNN


#If we ran this in code we would need to hold the session open to prevent the app server from exiting
session.wait()

# Codespaces doesn't play well with websockets or SSE so at the end of our URLs we need to put
# ?polling=true
# Which adds long polling
