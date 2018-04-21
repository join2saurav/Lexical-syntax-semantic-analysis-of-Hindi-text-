import collections
g=open("depth_31.txt","w")
with open('depth_22.txt') as infile:
    counts = collections.Counter(l.strip() for l in infile)
for line, count in counts.most_common():
    g.write(str(line))
    #g.write(str(count))
    g.write("\n")