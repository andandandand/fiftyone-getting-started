# FiftyOne Getting Started

## Overview
This repository provides an introduction to using [FiftyOne](https://voxel51.com/fiftyone/) for visualizing and managing computer vision datasets. FiftyOne is an open-source tool that enables easy exploration of datasets and model performance.

This guide walks you through:
- Loading datasets into FiftyOne
- Exploring and visualizing images
- Subsetting and querying data
- Generating and cleaning labels
- Evaluating and fine-tuning models

## Installation

### Option 1: GitHub Codespaces (Recommended)
1. Click the "Code" button above and select "Create codespace"
2. Wait for the environment to initialize
3. The environment will automatically:
   - Set up Python and required dependencies
   - Install MongoDB
   - Download sample images to `/photos/`
4. Note: When accessing the FiftyOne app in Codespaces, add `?polling=true` to the URL for better compatibility

### Option 2: Local Setup

#### Using Docker (Recommended for local setup)
1. Build and run the Docker container:
```sh
docker build -t fiftyone-demo .
docker run -it --rm \
  -p 5151:5151 \
  -p 27017:27017 \
  -v $(pwd):/workspace \
  fiftyone-demo
```
2. Access the FiftyOne app at `http://localhost:5151`

#### Manual Setup
##### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- pip
- MongoDB (FiftyOne requires it for dataset storage)

##### Setup
Clone this repository and install dependencies:
```sh
git clone <repo-url>
cd fiftyone-getting-started
pip install -r requirements.txt
```

If MongoDB is not running, start it manually:
```sh
mongod --fork --logpath /var/log/mongodb.log
```

## Development Environment
- The project includes a `.devcontainer/devcontainer.json` for consistent development setup
- Uses a custom container image with FiftyOne and MongoDB pre-installed
- Includes recommended VS Code extensions for Python development

## Dataset Structure
The repository uses several datasets:
- Initial quickstart dataset for basic exploration
- Custom photo dataset in `/photos/` for embedding and model training
- Pre-cleaned datasets available on HuggingFace:
  - Training data: "Voxel51/getting-started-labeled-photos"
  - Validation data: "Voxel51/getting-started-validation-clip-pred"

## File Organization
```
.
├── 0_app_tour.py          # Basic FiftyOne app introduction
├── 1_load_data.py         # Dataset loading examples
├── 3_viz_image_patterns.py # Image visualization and analysis
├── 4_subsetting_expressions.py # Dataset filtering
├── 5_generating_labels.py  # Label generation with CLIP
├── 7_fine_tune.py         # YOLO model fine-tuning
└── 8_evaluate_model.py     # Model evaluation
```

## Usage
Run the following scripts in order to explore the different functionalities of FiftyOne:
```sh
python 1_load_data.py  # Load dataset
python 3_viz_image_patterns.py  # Visualize patterns
python 4_subsetting_expressions.py  # Query and filter datasets
python 5_generating_labels.py  # Generate new labels
python 6_clean_labels.py  # Clean dataset labels
python 7_fine_tune.py  # Fine-tune a model on the dataset
python 8_evaluate_model.py  # Evaluate model performance
```

## Exploring FiftyOne
Once a dataset is loaded, launch the FiftyOne web app to explore it interactively:
```sh
fiftyone app
```

When using Codespaces:
1. The app will be available on port 5151
2. When prompted, click "Open in Browser" or navigate to the Ports tab
3. Add `?polling=true` to the end of the URL for better Codespace compatibility

## Troubleshooting
### MongoDB Process Stuck
If MongoDB does not start properly, find and kill the process manually:
```sh
for prc in /proc/*/cmdline; { (printf "$prc "; cat -A "$prc") | sed 's/\^@/ /g;s|/proc/||;s|/cmdline||'; echo; } | grep mongo
```
Then terminate it:
```sh
kill <process-id>
```

## Contributing
Feel free to submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.