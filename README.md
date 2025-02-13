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
### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- pip
- MongoDB (FiftyOne requires it for dataset storage)

### Setup
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
This opens a browser where you can inspect images, annotations, and model outputs.

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

