from __future__ import unicode_literals
from Tkinter import *
from tkFileDialog import *
import tkFont
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
i=694
f="<"
sen="Sentence id"
l=">"
gf="="
sen2=f+"/Sentence"+l

g = open("depth_8.txt","a")
with open("depth_11.txt","r") as f:
    lines=f.read().splitlines()
for line in lines:
    sen1 = "<"+ "Sentence id" +"="+ str(i)+ ">"
    g.write(sen1)
    g.write("\n")
    g.write(line)
    g.write("\n")
    g.write(sen2)
    g.write("\n")
    i=i+1
