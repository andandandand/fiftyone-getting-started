import fiftyone as fo
import fiftyone.zoo as foz

# Load the quickstart dataset
# This is a small dataset that ships with fiftyone
# It contains a few images and labels
# It's a good starting point for learning the library
dataset = foz.load_zoo_dataset("quickstart") 

session = fo.launch_app(dataset)

#If we ran this in code we would need to hold the session open to prevent the app server from exiting
session.wait()

# Codespaces doesn't play well with websockets or SSE so at the end of our URLs we need to put
# ?polling=true
# Which adds long polling
