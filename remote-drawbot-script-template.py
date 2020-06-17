"""
  This is a set of Python I use many times I wish to make an animation or multipage doc with Drawbot, 
  but code in my preferred editor (currently, VS Code) rather than in the Drawbot app.

  USAGE:

  First, install DrawBot as a module:

  pip install git+https://github.com/typemytype/drawbot
  
  Adapt script as needed, then run from the command line with:
  
  python3 <path>/remote-drawbot-script-template.py
"""

from drawBot import * # requires drawbot to be installed as module
import sys
import os

newDrawing() # required by drawbot module

# currentDir = sys.argv[0]
currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)
 
# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

docTitle = "drawbot-export" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True

fontFam = f"{currentDir}/fonts/name_sans-variable.trial.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 10
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "pdf" # pdf, gif, or mp4

pageSize = 3.5 # inches
DPI = 72 # dots per inch

paddingInPts = 18

# ----------------------------------------------
# Helper functions

pixels = DPI*pageSize # do not edit
W, H = pixels, pixels # do not edit
padding = DPI*paddingInPts/72 # do not edit

# turn font size into usable value for given pageSize
def computeFontSizePoints(pts):
	return W * (pts / (pageSize * 72))

# a frequently-useful function
def interpolate(a, b, t):
	return(a + (b-a) * t)

# ----------------------------------------------
# THE ACTUAL ANIMATION

for frame in range(frames):
	newPage(W, H) # required for each new page/frame

	t = frame / frames
	x = interpolate(0, W*0.9, t)
	
	font(fontFam, computeFontSizePoints(24)) # set a font and font size
	# draw text
	text("Name", (x, H/2))

endDrawing() # advised by drawbot docs

if save:
	import datetime

	now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # use "-%H_%M_%S" for more frequent versions

	if not os.path.exists(f"{currentDir}/{outputDir}"):
		os.makedirs(f"{currentDir}/{outputDir}")

	path = f"{currentDir}/{outputDir}/{docTitle}-{now}.{fileFormat}"

	print("saved to ", path)

	saveImage(path)

	if autoOpen:
		os.system(f"open --background -a Preview {path}")
