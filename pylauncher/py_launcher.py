#!/usr/bin/env python3
"""
notes for windows - 
needs to point to path to env python.exe - no need to activate
needs
    code path 
    repo path
    (optional) env folder name
    script path
"""

from pathlib import Path
from menuloop import display_menu
import subprocess
import os
import platform

# Get code path
CODE = Path(__file__).resolve().parent.parent.parent


OS = platform.system()

# Set up dict or class


class CMD:

    def __init__(self, repofolder, runptpath, envfolder=None) -> None:

        self.repofolder = CODE / repofolder
        self.runpath = self.repofolder / runptpath
        if envfolder:
            self.envfolder = self.repofolder / envfolder

    def send_commands(self) -> None:
        # write this to call the windows commands
        # cli > start env (if True) && launch .py

        if str(self.repofolder).endswith('EXIT'):
            exit('Exiting...')

        # Windows
        if OS == 'Windows':
            os.system(
                f'{self.envfolder/"Scripts"/"python.exe" if hasattr(self, "envfolder") else "py"} {self.runpath}')

        # Mac
        elif OS == 'Darwin':
            subprocess.run(
                f'{self.envfolder/"bin"/"python3" if hasattr(self, "envfolder") else "python3"} {self.runpath}', shell=True)

        else:
            exit('Platform not supported.')


def main():

    while True:
        # Display menu
        display_menu(
            ('Create Papercut Packages', CMD(
                'papercut-sw-packager',
                'pcswpkgr/papercut_sw_packager.py',
                envfolder='env'
            )),
            ('Compile MOR', CMD(
                'compile-MOR',
                'compmor/compile_mor.py',
                envfolder='env'
            )),
            ('Console Menu', CMD(
                'simple-console-menu',
                'menuloop.py',
                # envfolder=None
            )),
            ('Exit', CMD('EXIT', ''))
        ).send_commands()  # Send terminal command


if __name__ == "__main__":
    main()