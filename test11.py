
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

g = open("depth_30.txt","w")
with open("depth_29.txt","r") as f:
    lines=f.read().splitlines()
for line in lines:
    line1=line.replace("\u","")
    line2=line.replace(":","")
    g.write(line2)
    g.write("\n")