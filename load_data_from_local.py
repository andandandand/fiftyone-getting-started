import fiftyone as fo
import os

name = "jaguars_test"
dataset_dir = "/workspaces/fiftyone-getting-started/downloads/jaguars"


# Delete the dataset if it exists
try:
    dataset = fo.load_dataset(name)
    dataset.delete()
    print(f"Dataset '{name}' deleted.")
except fo.DatasetNotFoundError:
    print(f"Dataset '{name}' not found.")

# Create the dataset
dataset = fo.Dataset(name)

# Get the classnames (folder names)
class_names = os.listdir(dataset_dir)
print(f"Found {len(class_names)} class directories")

# Create samples
samples = []
for class_name in class_names:
    class_dir = os.path.join(dataset_dir, class_name)
    if not os.path.isdir(class_dir):
        continue  # Skip if not a directory

    image_count = 0
    for image_name in os.listdir(class_dir):
        if not image_name.endswith((".jpg", ".jpeg", ".png")):
            continue  # Skip if not an image

        image_path = os.path.join(class_dir, image_name)
        if os.path.exists(image_path):
            sample = fo.Sample(filepath=image_path, ground_truth=fo.Classification(label=class_name))
            samples.append(sample)
            image_count += 1
    
    print(f"Added {image_count} images for class '{class_name}'")

print(f"Total samples to add: {len(samples)}")
dataset.add_samples(samples)
print(f"Dataset now has {len(dataset)} samples")

# Launch the FiftyOne App with remote access enabled
session = fo.launch_app(dataset, remote=True)
print("FiftyOne app launched. Press Ctrl+C to exit.")

try:
    session.wait()
except KeyboardInterrupt:
    print("Session terminated by user")