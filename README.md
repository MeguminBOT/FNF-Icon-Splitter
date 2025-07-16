# Archived as the same functionality is now possible in https://github.com/MeguminBOT/TextureAtlas-to-GIF-and-Frames

# FNF Icon Splitter
This tool simplifies the process of extracting frames from icon spritesheets, organizing them into individual folders. 
It's designed to streamline your workflow by automating tedious tasks.

## Functionality
* Extracts and organizes frames of Friday Night Funkin icons 
Only tested on Psych Engine icons but should work for any icon sheet that is 150 pixels in height and is a multiple of 150 pixels in width

## Not yet implemented
* Selection of specific sprites for extraction (Currently processes entire folders).
* Improved user interface for enhanced usability.

## How to Install
### Windows
**Download**: [Get the executable here](https://github.com/MeguminBOT/FNF-Icon-Splitter/releases)

### Mac OSX
1. Download and Install Python 3.10+. You can download Python here: [https://www.python.org/downloads/](https://www.python.org/downloads/macos/)
2. Go to Applications > Utilities and open Terminal.
3. Type `python --version` to ensure that Python gets recognized by your system. If it returns the python version properly, proceed to step 4.
4. Type `python -m ensurepip`. After it's installed, make sure pip gets recognized by your system by typing: `pip --version` befoe proceeding to step 5.
5. Type `pip install pillow` to install PIL.
6. Type `pip install requests` to install Requests.

You should now be able to run the "FNF Icon Splitter.py" file by double clicking it. 
If not, then open a terminal window in the same folder as the script and type `python FNF Icon Splitter.py`, or drag and drop the file on the python application. 

### Linux (Ubuntu / Debian based)
1. Open the terminal.
2. Type `sudo apt install python3.10` and install (if it's not already installed).
3. Type `sudo apt install python3-pip` and install (if it's not already installed)
4. Type `sudo pip3 install pillow` to install PIL.
5. Type `sudo pip3 install requests` to install Requests.

You should now be able to run the "FNF Icon Splitter.py" file by double clicking it. 
If not, then open a terminal window in the same folder as the script and type `python3 FNF Icon Splitter.py`.
