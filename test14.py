import collections
g=open("depth_32.txt","w")
with open('depth_21.txt') as infile:
    counts = collections.Counter(l.strip() for l in infile)
for line, count in counts.most_common():
    g.write(str(line))
    #g.write(str(count))
    g.write("\n")