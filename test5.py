from __future__ import unicode_literals
from Tkinter import *
from tkFileDialog import *
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
import tkFont
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
g=open("depth_15.txt","w")
with open("depth_12.txt","r") as f:
    lines=f.read().splitlines()
for line in lines:
    line1=line.replace("<Sntn>","\n")
    line2=line1.replace("/u","")
    line3=line2.replace(",","")
    line4=line3.replace("-","")
    line5 = line4.replace("?", "")
    g.write(line5)
    g.write("\n")
