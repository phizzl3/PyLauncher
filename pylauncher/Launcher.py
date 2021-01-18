#!/usr/bin/env python3


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

    def __init__(self, repopath, runptpath, env=False) -> None:

        self.repopath = f'{CODE}{repopath}'
        self.runpath = f'{CODE}{runptpath}'
        self.env = env

    def send_commands(self) -> None:
        # write this to call the windows commands
        # cli > start env (if True) && launch .py

        if self.env == exit:
            exit('Exiting...')


        # Windows
        if OS == 'Windows':
            if self.env:
                os.system(
                    f'{self.repopath}/env/Scripts/activate && py {self.runpath}')
            else:
                os.system(f'py {self.runpath}')

        # Mac
        elif OS == 'Darwin':
            if self.env:
                subprocess.run(
                    f'source {self.repopath}/env/bin/activate && python3 {self.runpath}', shell=True)
            else:
                subprocess.run(f'python3 {self.runpath}', shell=True)

        else:
            exit('Platform not supported.')


def main():

    while True:
        # Display menu
        display_menu(
            ('Create Papercut Packages', CMD(
                '/papercut-sw-packager',
                '/papercut-sw-packager/pcswpkgr/papercut_sw_packager.py',
                env=True
            )),
            ('Exit', CMD(None, None, exit))
        ).send_commands()  # Send terminal command

if __name__ == "__main__":
    main()
