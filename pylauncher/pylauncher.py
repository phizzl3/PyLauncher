#!/usr/bin/env python3
"""
This script allows you to call other scripts located in repositories 
housed in the same parent folder as this script's cloned repository 
with a numbered menu by generating and sending your operating system's 
terminal/shell commands to launch them rather than you having to 
modify/import/combine them to do so.
* View README.md for more info.
"""

import json
import os
import platform
import subprocess
from pathlib import Path

import menu
import title

# Get Path to folder containing the repos and check operating system
# NOTE: If using pyinstaller to create an executable, remove the second
# and third .parent calls if the executable will be placed in the CODE
# directory

CODE = Path(__file__).resolve().parent.parent.parent
# CODE = Path(__file__).resolve().parent  # for pyinstaller use
OS = platform.system()

# NOTE: Set to True if having issues with commands to show shell message
SHOWRETURN = False


class CMD:

    def __init__(self, repofolder, runptpath, envfolder=None) -> None:
        """
        Initialize and set up attributes to be used to generate shell 
        commands.

        Args:
            repofolder (str): Folder name of the repo folder in the 
            folder containing the repos.
            runptpath (str): Filepath within the repofolder to your main 
            script that should be run for the given repo.
            envfolder (str, optional): Folder name within the repofolder 
            for your virtualenv folder if applicable. Defaults to None.
        """
        try:
            # Sets attributes containing Path objects pointing to
            # specified folders and file
            self.repofolder = CODE / repofolder
            self.runpath = self.repofolder / runptpath

            if envfolder:
                self.envfolder = self.repofolder / envfolder

        except Exception as e:
            input(f'\n Error running __init__: {e}')
            exit(' Exiting...')

    def send_commands(self) -> None:
        """
        Generates and runs shell commands based on detected operating 
        system and specified virtualenv if present. 
        (Windows, Mac, Linux)
        """
        # Set up an exit option to append to the end of the menu.
        if str(self.repofolder).endswith('EXIT'):
            exit(' Exiting...')
        try:
            # NOTE: Comment out if you don't want title shown once
            # selected script runs
            title.show()

            # Run formatted command based on detected OS and virtual
            # environment.
            if OS == 'Windows':
                os.system(
                    f'{self.envfolder/"Scripts"/"python.exe" if hasattr(self, "envfolder") else "py"} {self.runpath}')

            elif OS == 'Darwin' or 'Linux':
                subprocess.run(
                    f'{self.envfolder/"bin"/"python3" if hasattr(self, "envfolder") else "python3"} {self.runpath}', shell=True)

            else:
                exit('Platform not supported.')

        except Exception as e:
            input(f'\n Error running send_commands: {e}')
            exit(' Exiting...')


def main():
    """
    Walk CODE directory to locate PyLauncher.json files. Once located, 
    import data and generate menu items and CMD objects to execute 
    commands when selected.
    """
    selections = []
    for root, _dirs, files in os.walk(CODE):

        # If JSON file is found, read data
        if 'PyLauncher.json' in files:
            with open(Path(root) / 'Pylauncher.json', 'r') as json_file:
                jdata = json.loads(json_file.read())

            # Use JSON data to generate menu items and CMD objects
            selections.append((jdata['Display Info'], CMD(
                jdata['Project Folder'], jdata['Script Path'],
                jdata['Env Folder'])))

    # Add an exit option to the end of the list
    selections.append(('[ Exit ]', CMD('EXIT', '', '')))

    # Display menu and call commands on selection
    title.show()
    menu.display(*selections).send_commands()


if __name__ == "__main__":
    main()
