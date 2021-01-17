#!/usr/bin/env python3


from pathlib import Path
from menuloop import display_menu

import os


# Get code path
CODE = Path(__file__).resolve().parent.parent.parent
ENV = 'env/Scripts/activate'


# Set up dict or class
class CMD:

    def __init__(self, scrptpath, envpath=False) -> None:

        self.command = f'py {CODE}{scrptpath}'
        if envpath:
            self.environment = envpath

    def send_commands(self) -> None:
        # write this to call the windows commands
        # cli > start env (if True) && launch .py
        os.system(f'{CODE}{self.environment}{ENV} && {self.command}')
        pass


# Generate objects and list
def go():

    # Display menu
    display_menu(
        ('Create Papercut Packages', CMD(
            '/papercut-sw-packager/pcswpkgr/papercut_sw_packager.py', 
            '/papercut-sw-packager/'))
    ).send_commands()  # Send terminal command


if __name__ == "__main__":
    go()
