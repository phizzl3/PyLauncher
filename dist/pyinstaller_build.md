# pyinstaller build info

* Remove second and third .parent calls for resolving *CODE* Path at the
top of the __main__.py script.
* Open a shell
* Activate the virtual environment (Win)

```bash
$ .\env\Scripts\activate
```

* Install pyinstaller if not installed

```bash
$ pip install pyinstaller
```

* Run pyinstaller

```bash
$ pyinstaller --onefile --icon=images/purplealien.ico pylauncher/__main__.py
```

* Executable will be located in ***dist*** folder
* Delete other files that were created
* Rename .exe file

If there are issues running or building the file, try copying everything
into a single folder and running from there. Adjust file locations in 
pyinstaller command accordingly.
