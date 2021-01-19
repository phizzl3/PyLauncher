#!/usr/bin/env python3
"""

"""

from pathlib import Path
from menuloop import display_menu
import subprocess
import os
import platform

# Get Path to folder containing the repos and check operating system
CODE = Path(__file__).resolve().parent.parent.parent
OS = platform.system()


class CMD:

    def __init__(self, repofolder, runptpath, envfolder=None) -> None:

        self.repofolder = CODE / repofolder
        self.runpath = self.repofolder / runptpath
        if envfolder:
            self.envfolder = self.repofolder / envfolder

    def send_commands(self) -> None:

        # Set up an exit option to break out of the loop
        if str(self.repofolder).endswith('EXIT'):
            exit('Exiting...')

        # Run correctly formatted command based on detected OS and virtual environment
        if OS == 'Windows':
            os.system(
                f'{self.envfolder/"Scripts"/"python.exe" if hasattr(self, "envfolder") else "py"} {self.runpath}')

        elif OS == 'Darwin' or 'Linux':
            subprocess.run(
                f'{self.envfolder/"bin"/"python3" if hasattr(self, "envfolder") else "python3"} {self.runpath}', shell=True)

        else:
            exit('Platform not supported.')


def main():

    while True:
        # Generate objects and send to display menu (*EXAMPLES*)
        display_menu(
            ('_Menu option 1', CMD('_repo folder 1', '_src/main.py', envfolder='_env')),
            ('_Menu option 2', CMD('_repo folder 2', '_src2/main.py', envfolder='_venv')),
            ('_Menu option 3', CMD('_repo folder 3', '_src3/main.py', envfolder=None)),
            # Leave this one last for an exit option
            ('Exit', CMD('EXIT', ''))
            # Call send_commands method on object returned from menu selection
        ).send_commands()


if __name__ == "__main__":
    main()
