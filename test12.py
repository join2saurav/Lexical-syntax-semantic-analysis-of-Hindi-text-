from __future__ import unicode_literals
from Tkinter import *
from tkFileDialog import *
from nltk.tree import *
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
import tkFont
import re
import sys
import string

reload(sys)
sys.setdefaultencoding('utf-8')
g2=open("depth_22.txt","w")
g=open("depth_21.txt","r+")
g3=open("depth_23.txt","w+")
c=0
def check_val(st):
    g3.seek(0)
    lines = g3.readlines()
    for line in lines:
        t = len(line.split())
        #print t
        #print line.split()[:5]
        t1 = line.split()[:5]
        temp = ""
        for i in range(len(t1)):
            if i < 1:
                temp1 = t1[i]
            else:
                if temp == "":
                    temp = t1[i]
                else:
                    temp = temp + " " + t1[i]
        if temp==st:
            return temp1
        else:
            pass
    return "1"
def adjust(s,k):
    global c
    ln=len(s.split())
    t=1
    st="("
    for word in s.split():
        if t<ln-1:
            t=t+1
        else:
            st = st + " " + word
    st=st+" "+")"
    #print st
    val=check_val(st)
    #print val
    if val=="1":
        #if line.startswith(st.encode('utf-8'),3):
         #   print line
        c=c+1
        st2="X"+str(c)
    else:
        st2 = val
    st1= st2+" "+st
    g.write(st1)
    g.write("\n")
    g3.write(st1)
    g3.write("\n")

    t = 1
    ste = ""
    for word in s.split():
        if t < ln-1:
            t=t+1
        else:
            if ste=="":
                ste=word
                t=t+1
            else:
                ste = ste + " " + word
                t = t + 1
    #print ste
    st3=string.replace(s,ste,st2)
    return st3
def moreadjust(st):
    count = len(st.split())
    val=True
    while val:
        if count>2:
            st=adjust(st,count)
            count = len(st.split())
            #print st

        else:
            val = False
    st5 = "S" + " " + "(" + " " + st + " " + ")"
    g2.write(st5)
    g2.write("\n")
with open('depth_30.txt','r') as f:
    for line in f:
        i=1
        k=0
        s=''
        for word in line.split():
            if i<3:
                i=i+1
                #print word
            elif word==")":
                pass
            else:
                k=k+1
                if s=='':
                    s=word
                else:
                    s=s+" "+word
        if k>2:
            #print s
            st4=adjust(s,k)
            moreadjust(st4)
        else:
            g2.write(line)
            g2.write("\n")

            #print c