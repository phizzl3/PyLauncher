# PyLauncher

Pull together individual scripts/repos from a folder and launch them using the command line.

## What it does

This script allows you to call other scripts located in repositories housed in the same folder as this script's cloned repository with a numbered menu using your operating system's terminal/shell commands rather than having to modify/import/combine hem to do so.  

* Works with or without a virtualenv in each given repo.  
* Generates commands based on detected operating system.  
* Written for Windows, Mac, and Linux.  
* Includes an example batch file for Windows. Edit with your specific Path to run the launcher without needing to open python or an editor.  

## Why?  

The idea is to have a central folder that you clone all of your repositories into, including this one, and then use this repository's launcher to run the other scripts contained in those adjacent repos using shell commands rather than having to combine the scripts and make changes or import them into a central script and try to figure out how to make everything work together with multiple virtual environments and possible conflicts, etc.  This, instead lets you develop standalone scripts and just call them from this launcher without any changes needed.  

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

Replace the Example info in the script with your repo's info and run it.  
