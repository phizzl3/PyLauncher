#!/usr/bin/env python3


from pathlib import Path





# Get code path
CODE = Path(__file__).resolve().parent.parent.parent
ENV = '.\env\Scripts\activate'


# Set up dict or class
class Launch:

    def __init__(self, cmd, env=False) -> None:

        self.command = cmd
        if env:
            self.environment = env

    def send_commands(self) -> None:
        # write this to call the windows commands
        # cli > start env (if True) && launch .py
        pass




# Generate objects and list
def go():

    menufunc(
        ('Create Papercut Packages', CMD(
            'this is the command to start',
            'this is the env command'
        ))
    ).call_commands_method()

# Display menu
# Send terminal command









































