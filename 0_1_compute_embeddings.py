import fiftyone as fo
import fiftyone.brain as fob
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")

# Image embeddings
fob.compute_visualization(dataset, brain_key="img_viz")

# Object patch embeddings
fob.compute_visualization(
    dataset, patches_field="ground_truth", brain_key="gt_viz"
)

session = fo.launch_app(dataset)

session.wait()
