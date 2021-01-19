#!/usr/bin/env python3
"""
This script allows you to call other scripts located in repositories 
housed in the same folder as this script's cloned repository with a 
numbered menu using your operating system's terminal/shell commands 
rather than having to modify/import/combine them to do so. Works with 
or without a virtualenv in each given repo. View README.md for more info.
"""

import os
import platform
import subprocess
from pathlib import Path

from menuloop import display_menu
from title import display_title

# Get Path to folder containing the repos and check operating system
CODE = Path(__file__).resolve().parent.parent.parent
OS = platform.system()


class CMD:

    def __init__(self, repofolder, runptpath, envfolder=None) -> None:
        """
        Initialize and set up attributes to be used to generate shell commands.

        Args:
            repofolder (str): Folder name of the repo folder in the folder 
                containing the repos.
            runptpath (str): Filepath within the repofolder to your main 
                script that should be run for the given repo.
            envfolder (str, optional): Folder name within the repofolder 
                for your virtualenv folder if applicable. Defaults to None.
        """
        try:
            # Sets attributes containing Path objects pointing to specified folders and file
            self.repofolder = CODE / repofolder
            self.runpath = self.repofolder / runptpath
            
            if envfolder:
                self.envfolder = self.repofolder / envfolder

        except Exception as e:
            input(f'\n Error running __init__: {e}')
            exit(' Exiting...')

    def send_commands(self) -> None:
        """
        Generates and runs shell commands based on detected operating system and 
        specified virtualenv if present. (Windows, Mac, Linux)
        """
        try:
            # Set up an exit option to break out of the loop
            if str(self.repofolder).endswith('EXIT'):
                exit(' Exiting...')

            # Run correctly formatted command based on detected OS and virtual environment
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
    Generates objects, displays the selection menu and calls the 
    send_commands method on returned object based on user selction.
    """
    try:
        while True:
            display_title()
            # Generate objects and send to display menu (*EXAMPLES*)
            display_menu(('_Menu option 1', CMD('_repo folder 1', '_src/main.py', envfolder='_env')),
                ('_Menu option 2', CMD('_repo folder 2', '_src2/main.py', envfolder='_venv')),
                ('_Menu option 3', CMD('_repo folder 3', '_src3/main.py', envfolder=None)),
                # Leave this one last for an exit option
                ('Exit', CMD('EXIT', ''))
            ).send_commands()  # Call send_commands method on object returned from menu selection

    except Exception as e:
        input(f'\n Error running main: {e}')
        exit(' Exiting...')


if __name__ == "__main__":
    main()
