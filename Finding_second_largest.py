n = int(input())
list1=list(map(int,input().split()))

list1.sort()
x= list1[-1]

while x in list1:
   list1.remove(x)
 
 print(max(list1))
