"""
Generated using: 
http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""


import os
import platform
import subprocess

import colorama

# Get operating system
OS = platform.system()

# Set up colorama output
colorama.init(autoreset=True)
BLUE = colorama.Fore.LIGHTBLUE_EX


def show():
    """
    Clears screen and displays ASCII art to console based on OS.
    """
    title = """
 ██████╗ ██╗   ██╗██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
 ██╔══██╗╚██╗ ██╔╝██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗
 ██████╔╝ ╚████╔╝ ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝
 ██╔═══╝   ╚██╔╝  ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗
 ██║        ██║   ███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║
 ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                       Code: Brandon
    """

    if OS == 'Windows':
        os.system('cls')
    elif OS == 'Darwin' or OS == 'Linux':
        subprocess.run('clear', shell=True)

    print(f'{BLUE}{title}')


if __name__ == "__main__":
    # Test
    show()
