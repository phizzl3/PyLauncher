"""
Generated using: 
http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""


import os
import platform
import subprocess

# Get operating system
OS = platform.system()


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
                                                                       
    """

    if OS == 'Windows':
        os.system('cls')
    elif OS == 'Darwin' or OS == 'Linux':
        subprocess.run('clear', shell=True)

    print(title)


if __name__ == "__main__":
    # Test
    show()
