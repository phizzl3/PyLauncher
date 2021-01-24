#!/usr/bin/env python3
"""
This script allows you to call other scripts located in repositories housed in the 
same parent folder as this script's cloned repository with a numbered menu by 
generating and sending your operating system's terminal/shell commands to launch 
them rather than you having to modify/import/combine them to do so.
* View README.md for more info.
"""

import os
import platform
import subprocess
from pathlib import Path

import menu
import options
import title

# Get Path to folder containing the repos and check operating system
CODE = Path(__file__).resolve().parent.parent.parent
OS = platform.system()

# Set to True if having issues with commands to show shell message
SHOWRETURN = False

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
            title.show()  # NOTE: Comment out if you don't want title shown once selected script runs
            # TODO: Set up an exit option to break out of the loop
            if str(self.repofolder).endswith('BACK'):
                return
            elif str(self.repofolder).endswith('EXIT'):
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
    send_commands method on returned object based on user selection.
    """
    try:
        while True:
            title.show()
            # NOTE: Add your menu options to OPS in menuoptions.py
            sel = menu.display(
                ('Print Shop Programs', options.PSP), ('Spreadsheet Processing', options.SSP), 
                ('MDS/Print Management Programs', options.MDS), ('[ Exit ]', 'EXIT'))
            
            if sel == 'EXIT':
                exit( 'Exiting...')

            # Generate objects and menu items
            selections = [(d, CMD(rf, rp, envfolder=ef))
                          for d, rf, rp, ef in sel]
            title.show()
            # Display menu and call send_commands method on returned object
            menu.display(*selections).send_commands()

            if SHOWRETURN:
                input(' ENTER to close...')

    except Exception as e:
        input(f'\n Error running main: {e}')
        exit(' Exiting...')


if __name__ == "__main__":
    main()
