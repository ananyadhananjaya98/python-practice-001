numofcommands = int(input())
l=[]
for i in range(numofcommands):
    List1 = input().split()
    a = List1[0]
    b = List1[1:]
    if a != "print":
        #insert(5,0)
        a+="("+",".join(b)+")"
        eval("l."+a)
    else:
        print(l)
