#!/usr/bin/env python3


from pathlib import Path
from menuloop import display_menu




# Get code path
CODE = Path(__file__).resolve().parent.parent.parent
ENV = '.\env\Scripts\activate'


# Set up dict or class
class CMD:

    def __init__(self, cmd, env=False) -> None:

        self.command = cmd
        if env:
            self.environment = env

    def send_commands(self) -> None:
        # write this to call the windows commands
        # cli > start env (if True) && launch .py
        print(self.command)
        pass




# Generate objects and list
def go():

    # Display menu
    display_menu(
        ('Create Papercut Packages', CMD(
            'this is the command to start',
            'this is the env command'
        ))
    ).send_commands() # Send terminal command



































if __name__ == "__main__":
    go()





