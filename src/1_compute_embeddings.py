import fiftyone as fo
import fiftyone.brain as fob
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")

# Image embeddings
fob.compute_visualization(dataset, brain_key="img_viz")

# Object patch embeddings
# We use small a batch_size and num_workers=0 to avoid running out of memory
fob.compute_visualization(
    dataset,
      patches_field="ground_truth",
      brain_key="gt_viz", 
      batch_size=2,
      num_workers=0
)

session = fo.launch_app(dataset)

session.wait()
