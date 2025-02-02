System Cleaner Utility
A simple Python utility to clean temporary files and empty the recycle bin on Windows systems.

Features
Cleans temporary files from the system's TEMP directory
Empties the Windows Recycle Bin
Error handling for file operations
Console output for operation status
Requirements
Python 3.x
winshell library for Recycle Bin operations
Installation
Clone or download this repository
Install the required dependency:
pip install pywin32
Usage
Run the script with Python:
python limpieza.py
Functions
The utility includes two main functions:

limpiar_temporales(): Removes all files and directories from the system's TEMP folder
vaciar_papelera(): Empties the Windows Recycle Bin
Notes
Requires administrative privileges to delete certain temporary files
Some files may be locked by the system and cannot be deleted
Error messages will be displayed for files that cannot be deleted
Error Handling
The script includes error handling for:

File access permissions
Locked files
Missing winshell library
Recycle bin operations
