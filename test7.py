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
g=open("depth_16.txt","w")
with open("depth_15.txt","r") as f:
    lines=f.read().splitlines()
for line in lines:
    line1=line.replace("(NP ","NP ( ")
    line2=line1.replace("(VP ","VP ( ")
    line3= line2.replace("(A ", "A ( ")
    line4= line3.replace("(B ", "B ( ")
    line5= line4.replace("(RBP ", "RBP ( ")
    line6= line5.replace("(E ", "E ( ")
    line7= line6.replace("(VP ", "VP ( ")
    line8= line7.replace("(JJP ", "JJP ( ")
    line9= line8.replace("(VP ", "VP ( ")
    line10 = line9.replace("(D ", "D ( ")
    line11=line10.replace("(S ","S ( ")
    line12=line11.replace("S( ","S ( ")
    line13=line12.replace(")"," )")
    g.write(line13)
    g.write("\n")

