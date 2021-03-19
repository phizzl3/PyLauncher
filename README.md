# PyLauncher

Pull together individual scripts/repos from a folder and launch them using
shell commands via a menu.

![Sample Window](/images/pylauncher.jpg)

## What it does

This script allows you to call other scripts located in repositories housed in
the same parent folder as this script's cloned repository with a numbered menu
by generating and sending your operating system's terminal/shell commands to
launch them rather than you having to modify/import/combine each script to do
so by using a customized ***PyLauncher.json*** file that is located in the
*json* folder.

* Works with or without a virtualenv in each given repo. (with is recommended)
* Generates shell commands based on detected operating system.
* Automatically adds repos/scripts based on a JSON file that you edit and copy
to your repo's folder. 
* Written for Windows, Mac, and Linux.  
* Includes an example batch file for Windows located in the *batch* directory.
Edit with your specific Path to run the launcher without needing to open python
or an editor.
* Also includes ***PyLauncher.exe*** file for Windows located in the *dist*
directory. Copy this file into the root folder where you have your code/repos
and run from there.  

## Why?  

The idea is to have a central folder that you clone all of the repositories you
want to easily launch into, including this one or the executable, and then use
this repository's launcher to run the other scripts contained in those adjacent
repos using a menu that sends shell commands rather than having to combine the
scripts and make changes or import them into a central script and try to figure
out how to make everything work together with multiple virtual environments and
possible conflicts, etc.  This script instead, lets you develop standalone
scripts and just call them from this launcher without any changes needed to
those individual scripts...only a single file that you copy to the directory.

## Sample folder structure

```txt
code/
├── PyLauncher
│   ├── LICENSE
│   ├── pylauncher
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── menu.py
│   │   └── title.py
│   └── README.md
├── Repo-1
│   ├── PyLauncher.json
│   ├── README.md
│   ├── repo1
│   │   ├── __init__.py
│   │   └── __main__.py
│   └── venv
├── Repo-2
│   ├── PyLauncher.json
│   ├── LICENSE
│   ├── README.md
│   └── repo_2.py
└── Repo-3
    ├── PyLauncher.json
    ├── env
    ├── LICENSE
    ├── README.md
    └── src
        ├── data.py
        └── repo3.py
```

## PyLauncher.json Usage

Copy this file from the *json* folder to somewhere in each of your project
folders, update the information to match that specific project, and rename the
file to ***PyLauncher.json*** (remove leading underscore).

### Content Structure

```json
{
    "Display Info": "PyLauncher Demo",
    "Project Folder": "PyLauncher",
    "Script Path": "pylauncher/__main__.py",
    "Env Folder": "env"
}
```

* "Display Info" - This is what will display as the menu choice in the launcher
menu.
* "Project Folder" - This should be the folder name of the top-level
folder/repo containing the project.
* "Script Path" - This is the path, including subfolders from the top-level
folder to the main script that should run when selected.
* Env Folder" - This is the directory name of the projects virtual environment
folder if the project has one. If there is no virtal environment in use, set
this to ***null*** - (No quotes, etc).
