# Get Numbers

This project is a python script aiming to generate numbers from 1 to 10 in random order.


## Running program on macOS
macOS since version 10.8 comes with Python 2.7 pre-installed by Apple. If you wish, you may install the most recent version of Python 3 from the Python website (https://www.python.org). 

What you get after installing is a number of things:

A Python 3.9 folder in your Applications folder. In here you find IDLE, the development environment that is a standard part of official Python distributions; and PythonLauncher, which handles double-clicking Python scripts from the Finder.

A framework /Library/Frameworks/Python.framework, which includes the Python executable and libraries. The installer adds this location to your shell path. To uninstall MacPython, you can simply remove these three things. A symlink to the Python executable is placed in /usr/local/bin/.

The Apple-provided build of Python is installed in /System/Library/Frameworks/Python.framework and /usr/bin/python, respectively. You should never modify or delete these, as they are Apple-controlled and are used by Apple- or third-party software. Remember that if you choose to install a newer Python version from python.org, you will have two different but functional Python installations on your computer, so it will be important that your paths and usages are consistent with what you want to do.

### How to run a Python script
The best way to get started with Python on macOS is through the IDLE integrated development environment

If you want to run Python scripts from the Terminal window command line or from the Finder you first need an editor to create your script. macOS comes with a number of standard Unix command line editors, vim and emacs among them.

To run your script from the Terminal window you must make sure that /usr/local/bin is in your shell search path.

To run your script from the Finder you have two options:

Drag it to PythonLauncher

Select PythonLauncher as the default application to open your script (or any .py script) through the finder Info window and double-click it. PythonLauncher has various preferences to control how your script is launched. Option-dragging allows you to change these for one invocation, or use its Preferences menu to change things globally.


## Running program on Linux

Save the generateNumbers.py file to a specific location in your system and then follow the steps below to run it:

Open the terminal by searching for it in the dashboard or pressing Ctrl + Alt + T.

Navigate the terminal to the directory where the script is located using the cd command.

Type python generateNumbers.py in the terminal to execute the script.

If the script is python3, use python3 in the terminal command:python3 getNumbers.py



## Acknowledgments

* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* https://stackoverflow.com/
* https://docs.python.org/
* https://replit.com/
