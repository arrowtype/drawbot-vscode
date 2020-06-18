# Using DrawBot in VS Code (or any external code editor)

This post is made to accompany a talk at the 2020 Typographics TypeLab, but aims to be useful as a standalone resource.

## Basics

### What is DrawBot?

- [DrawBot](https://www.drawbot.com/) is a macOS app for generating graphics with Python.
- Also available as [a Python module](https://github.com/typemytype/drawbot), for use in any coding environment (VS Code, Sublime, BB Edit, etc)
- Requires macOS, because it uses Mac text & graphics APIs

### What is VS Code?

[Visual Studio Code](https://code.visualstudio.com/) is a free source-code editor made by Microsoft for Windows, Linux and macOS. 

For the purpose of using DrawBot in VS Code, macOS is still required.

### Starting a script in DrawBot

- The docs are really good for an introduction, and it this session isn’t meant to be an introduction

### Why use the DrawBot Python module in VS Code?

A good text editor is a massive software project (VS Code is backed by Microsoft & a huge open-source community), and the DrawBot maintainers have wisely focused on making a graphics library and keeping the DrawBot app as a simple product.

- Comfort
  - DrawBot doesn’t use usual code syntax highlighting theme, and it’s tedious to configure colors.
  - VS Code has extensions that help readability, like [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
  - The DrawBot app can be tricky to update: automatic updates don’t work for me (this could be a macOS security thing). Because I can only update by downloading a new installation from the website, my preferences get erased each time. Goodbye, theme edits. :( By contrast, VS Code just updates without me doing anything, leaving my settings intact.

- Speed
  - Familiar shortcuts (I spend a lot of time in VS Code)
  - Multi-selection & editing (e.g. for variable renaming)
  - Multi-line editing
  - Moving lines up & down with key commands

- Context
  - Built-in tools in VS Code: file explorer, source control panel, file diffing, and more
  - Python linting in VS Code (though, I am still working on utilizing this properly)

### Where DrawBot is better

- “Drawing” with numbers is very cool
- Faster preview updates
- `Command r` refresh preview

## How to work with DrawBot in VS Code

### The basics

First, install DrawBot as a module:

```bash
pip install git+https://github.com/typemytype/drawbot
```

Near the top of your file, you’ll need these two lines:

```python
from drawBot import *             # requires drawbot to be first installed as module
newDrawing()                      # required by drawbot module

# do your usual drawbot stuff here
text("hello drawbot", (500,500))

endDrawing()                      # advised by drawbot docs

path = "./hello-drawbot.pdf"      # set the path as a variable
saveImage(path)                   # make sure to save your image

# not required, but functions as an instant preview
import os
os.system(f"open --background -a Preview {path}")
```

You can actually do this in fewer lines of code, but that is about as simple as I can make it while still keeping it useful.

Finally, run this python file in a terminal with:

```bash
python3 PATH_TO_DRAWBOT_SCRIPT.py
```

### Make it simpler to run your DrawBot script

You probably don’t want to type in the terminal a lot.

In VS Code: 

1. Install the VS Code extension [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2. Pull up the command palette with **Command Shift P**. Then search `Python: Run Python File in Terminal`

If step 2 doesn’t work, you may have to go into VS Code settings (**Command comma**) and search `Python: Python Path`, and set this to “Python3”.

**MAKE IT EVEN FASTER**

From the Command Palette (**Command Shift P**), select `Preferences: Open Keyboard Shortcuts File`.

Search `Python: Run Python File in Terminal`. Click the `+` icon, and enter **Command R** or whatever shortcut you want. (**Command R** will override the “Refresh Window” shortcut, but if you’re like me, you will use this less than running Python files, so searching for it in the Command Palette is a fine tradeoff.)

### Workflow Tips

- This workflow relies on saving new files for previews, so you should adjust the timestamp as needed to overwrite or not overwrite exports as needed
  - A good default is letting timestamps have `year_month_day-hour_minute`. That way, as you generate, you will only be left with a new file for each minute of work.
  - If you are making lots of experimental changes and you aren’t worried about saving computer disk space, add `_seconds` to your timestamp and go nuts!
  - If you *are* worried about disk space (e.g. you are exporting large gif files, etc), maybe just go by the `hour`, and change the file name when you actually want to save a specific version. 
- It’s also useful to version with Git, but that deserves its own workshop
- You will occassionally hit a limit on macOS preview where it will stop opening new files. At this point, you will have to click on one of the Preview windows, and use the shortcut **Option Command W** to close all open windows.

------------------------------------------------------------------

## VS Code links

- My code theme: https://github.com/arrowtype/recursive-theme
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

## Fonts used

This uses Recursive VF 1.031, available as an OFL on GitHub ([permalink](https://github.com/arrowtype/recursive/blob/006828dd941878bf0819a97c9d6286f24972bb16/fonts_1.031/Variable_TTF/Recursive_VF_1.031.ttf)).

This also uses a trial version of Name Sans, available from [Future Fonts](https://www.futurefonts.xyz/arrowtype/name-sans).

## Example scripts on GitHub

- [Recursive Hearts](https://github.com/arrowtype/recursive/tree/2c1c9d58e2130851cd6cee804d71ccce73b75805/src/proofs/drawbot-specimens-and-diagrams/hearts)
- [Recursive Flipbook](https://github.com/arrowtype/recursive/blob/2c1c9d58e2130851cd6cee804d71ccce73b75805/src/proofs/drawbot-specimens-and-diagrams/flipbook/recursive-flipbook-wave_viz-multistage-visualization_2-outlined_text-081419.drawbot.py)

## Please do these two things

1. Check out https://arrowtype.github.io/vf-slnt-test/slnt-ital-tests/index.html, scroll to the bottom, and follow links to the Chromium & WebKit issues to voice your support for the prioritization of fixing the rendering of slnt & ital variable axes.

2. Check out https://github.com/fonttools/fonttools/issues/1994 & let me know if you have experienced the same font-menu issue in other fonts or if you know a solution (but this is probably a macOS issue, so at the very least it would be good to show that many people are having trouble here)
