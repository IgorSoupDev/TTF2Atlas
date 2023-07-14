# Install Guide
This guide will walk you through the process of install everything you need for execute the `ttf2atlas.py`.

# Requirements
- Python 3.x installed
- Pillow (PIL fork) package installed

If you already have Python and Pillow installed in your machine you can skip to [Executing the script](#executing-the-script).

## How install Python
### Windows:
If you are using MinGW you can get Python by using the following command: `pacman -S mingw-w64-x86_64-python`

Otherwise follow the steps below.
- Visit the official Python website at https://www.python.org/.
- Click on the `Downloads` tab.
- On the downloads page, you'll see the latest version of Python. To install Python 3, select the latest version that starts with `3.x.x.`
- Once you've downloaded the installer, locate the downloaded file and double-click on it to run the installer.
- In the installer window, make sure to check the box that says `Add Python to PATH` to enable command-line access to Python.
- Proceed with the default installation options unless you have specific preferences.
- Once the installation is complete, you can verify it by opening the Command Prompt and typing `python --version`. It should display the installed Python version.

### macOS:
macOS typically comes with a pre-installed version of Python. To check if Python is already installed, open the Terminal and type `python --version`. If a version is displayed, Python is already installed. If not, follow the steps below.
- Visit the official Python website at https://www.python.org/.
- Click on the `Downloads` tab.
- On the downloads page, you'll see the latest version of Python. To install Python 3, select the latest version that starts with 3.x.x.
- Once you've downloaded the installer, locate the downloaded file and double-click on it to run the installer.
- In the installer window, follow the prompts and proceed with the installation.
- Once the installation is complete, you can verify it by opening the Terminal and typing `python3 --version`. It should display the installed Python version.

### Linux:
Python is often pre-installed on Linux distributions. To check if Python is already installed, open a terminal and type `python --version` or `python3 --version`. If a version is displayed, Python is already installed. If not, follow the steps below.
- Open the terminal and update the package list by running the following command: `sudo apt update`
- Install Python by running the following command: `sudo apt install python3`
After the installation is complete, you can verify it by typing `python3 --version` in the terminal. It should display the installed Python version.

## How to Install the Dependencies
### Windows:
If you are using MinGW, you can install the dependencies by using the command `python3 -m pip install -r requirements.txt`. If not, use `py -3 -m pip install -r requirements.txt`.

### Linux/MacOS:
Use the following command: `python3 -m pip install -r requirements.txt`.

# Executing the script
- Download the repository and save it in a directory of your choice.
- Open a command prompt or terminal and navigate to the directory where the repo is located.
- Run the script by executing the following command: `python ttf2atlas.py` or `python3 ttf2atlas.py` if the first one doesn't work
- This should generate `arial.png` and `arial.h` in the example folder
