# PyLauncher

Pull together individual scripts/repos from a folder and launch them using shell commands via a menu.

![Sample Window](/images/pylauncher.jpg)

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
code/
├── PyLauncher
│   ├── LICENSE
│   ├── pylauncher
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── menu.py
│   │   ├── options.py
│   │   ├── PyLauncher.bat
│   │   ├── py_launcher.py
│   │   └── title.py
│   └── README.md
├── Repo-1
│   ├── README.md
│   ├── repo1
│   │   ├── __init__.py
│   │   └── __main__.py
│   └── venv
├── Repo-2
│   ├── LICENSE
│   ├── README.md
│   └── repo_2.py
└── Repo-3
    ├── env
    ├── LICENSE
    ├── README.md
    └── src
        ├── data.py
        └── repo3.py
```

Replace the example info listed below and run py_launcher.py.  

```py
# Replace each group within the OPS list in menuoptions.py with your repo/script/folder info

OPS = (
    
    # Using example from above
    ('Repo 3', 'Repo-3', 'src/repo3.py', 'env'),

)
```

Run  

```bash
$ py pylauncher
```
