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
