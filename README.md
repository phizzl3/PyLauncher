# PyLauncher

Pull together individual scripts/repos from a folder and launch them using shell commands via a menu.

## What it does

This script allows you to call other scripts located in repositories housed in the same parent folder as this script's cloned repository with a numbered menu by generating and sending your operating system's terminal/shell commands to launch them rather than you having to modify/import/combine each script to do so.  

* Works with or without a virtualenv in each given repo.  
* Generates shell commands based on detected operating system.  
* Written for Windows, Mac, and Linux.  
* Includes an example batch file for Windows. Edit with your specific Path to run the launcher without needing to open python or an editor.  

## Why?  

The idea is to have a central folder that you clone all of the repositories you want to easily launch into, including this one, and then use this repository's launcher to run the other scripts contained in those adjacent repos using a menu that sends shell commands rather than having to combine the scripts and make changes or import them into a central script and try to figure out how to make everything work together with multiple virtual environments and possible conflicts, etc.  This script instead, lets you develop standalone scripts and just call them from this launcher without any changes needed to those individual scripts.  

## Sample folder structure

```txt
-code_folder
    -pylauncher
        -pylauncher
            -PyLauncher.bat
            -PyLauncher.py
    -repo1
        -venv
        -src
            -main.py
    -repo2
        -main2.py
    -repo3
        -env
        -python
            -main.py
```

Replace the Example info in the PyLauncher.py script's main function with your repo's info and run it.  

```py
# Replace each set within the display_menu call below with your repo/script/folder info
display_menu(

    ('Displays in menu', CMD('RepoFolderName', 'myscript.py', envfolder='EnvironmentFolder'),

    ).send_commands()
```
