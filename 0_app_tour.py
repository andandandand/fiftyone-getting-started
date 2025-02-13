import fiftyone as fo

fo.list_datasets()

dataset = fo.load_dataset("quickstart")

session = fo.launch_app(dataset)

#If we ran this in code we would need to hold the session open to prevent the app server from exiting
session.wait()

# Codespaces doesn't play well with websockets or SSE so at the end of our URLs we need to put
# ?polling=true
# Which adds long polling
