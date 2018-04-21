import re
import sys
reload(sys)
#sys.setdefaultencoding('utf-8')

g = open('depth_12.txt','w')
f = open('depth_27.txt','r')
for line in f.read().split("\n"):
    if line.startswith("<Sentence"):
        g.write(line)
        g.write("\n")
    else:
    #line1=line.replace("","_")
        line1=line.replace("\u09","")
        line2 = line1.replace("/", "")
        line3 = line2.replace("0", "")
        line4 = line3.replace("1", "")
        line5 = line4.replace("2", "")
        line6 = line5.replace("3", "")
        line7 = line6.replace("4", "")
        line8 = line7.replace("5", "")
        line9 = line8.replace("6", "")
        line10 = line9.replace("7", "")
        line11= line10.replace("8", "")
        line12 = line11.replace("9", "")
        line13 = line12.replace("a", "")
        line14 = line13.replace("b", "")
        line15 = line14.replace("c", "")
        line16 = line15.replace("d", "")
        line17 = line16.replace("e", "")
        line18 = line17.replace("f", "")
        g.write(str(line18))
g.close()
f.close()



