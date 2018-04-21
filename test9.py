class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
i=0
lst=[]
def make_stack():
    return Stack()
stk=make_stack()
lst.append(stk)
g=open("depth_28.txt","w")
with open('depth_16.txt','r') as f:
    for line in f:
        for word in line.split():

#with open("depth_17.txt") as fileobj:
    #for word in fileobj:
        #for ch in word:
            if lst[i].peek!="S":
                if word=='(':
                    pk=lst[i].peek()
                    stk1=make_stack()
                    lst.append(stk1)
                    i=i+1
                    lst[i].push(pk)
                    lst[i].push(word)
                elif word==')':
                    st=')'
                    while lst[i].isEmpty() == False:
                        st = lst[i].pop() +' '+st
                    #print st
                    g.write(st)
                    g.write("\n")
                    i=i-1
                else:
                    lst[i].push(word)
            else:
                lst[i].push(word)
