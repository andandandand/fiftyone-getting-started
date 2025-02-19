# FiftyOne Getting Started

## Overview
This repository provides an introduction to using [FiftyOne](https://voxel51.com/fiftyone/) for visualizing and managing computer vision datasets. FiftyOne is an open-source tool that enables easy exploration of datasets and model performance.

This guide walks you through:
- Loading datasets into FiftyOne
- Exploring and visualizing images


## Installation

## Development Environment
- The project includes a `.devcontainer/devcontainer.json` for consistent development setup
- Uses a custom container image with FiftyOne and MongoDB pre-installed
- Includes recommended VS Code extensions for Python development

### Option 1: Cloud Execution with GitHub Codespaces (Recommended)
1. Click the "Code" button above and select "Create codespace"
2. Wait for the environment to initialize
3. The environment will automatically:
   - Set up Python and required dependencies
   - Install MongoDB
   - Download sample images to `/photos/`
4. Note: When accessing the FiftyOne app in Codespaces, add `?polling=true` to the URL for better compatibility

When using Github Codespaces:
1. The app will be available on port 5151
2. When prompted, click "Open in Browser" or navigate to the Ports tab
3. Add `?polling=true` to the end of the URL for better Codespace compatibility

### Option 2: Local Setup 

1. Download the repository into your local computer and open it with [VSCode](https://code.visualstudio.com/).
2. Download the [Dev Container VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. When opening the project folder, VSCode will detect that there is a `devcontainer.json` file defined. Click "Reopen in Container"


#### Option 3: Manual Setup (not using the devcontainer)
##### Prerequisites
Ensure you have the following installed:
- A version of Python between 3.9 and 3.11
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


## Exploring FiftyOne
Once a dataset is loaded, launch the FiftyOne web app to explore it interactively:
```sh
fiftyone app
```

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