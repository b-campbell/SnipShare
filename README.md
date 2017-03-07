# SnipShare

SnipShare is a Sublime Text 3 Plugin designed to allow easy saving and recalling of segments of code (code snippets).
Simply highlight the code you want to save and name the code snippet.
The next time you type in the name of that snippet into Sublime Text, an option in the autocomplete interface will allow you to paste that code snippet into your file.

[Example of SnipShare functionality](docs/example.png)

Features:
* Quick and easy saving: Use the ctrl+shift+x (command+shift+x for mac) shortcut or right-click-> create Snippet to activate the plugin.
* Quick snippet recall system: Use Sublime Text's built in autocomplete interface to restore saved snippets of specific names.
* Context-aware: X language snippets can't be recalled while programming in language Y.
* Multi-platform: Compatible with Windows and Unix based operating systems.

Installation guide:
Set the USER_FOLDER variable in snipshare.py to the ABSOLUTE PATH to your Sublime Text 3 User preferences file.
* In Linux: "~/.config/sublime-text-3/Packages/User"
* In Windows: "C:\\Users\\YOUR_USERNAME\\AppData\\Roaming\\Sublime Text 3\\Packages\\User"

DONE! You can now use SnipShare.

Usage:
* Highlight a code block you want to save.
* Either Right-Click and press Create Snippet, or press ctrl+shift+x (command+shift+x for mac).
* Enter your description/ name for the snippet in the text box at the bottom of Sublime Text (Note this description is what you want to type to recall the code later).
* When you start writing that description/ name again in Sublime Text, a suggestion in the autocomplete window will show your snippet. Press enter with it selected to paste your saved snippet.
