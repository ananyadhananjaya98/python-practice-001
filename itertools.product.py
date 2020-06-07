from itertools import product

A = input().split()
B = input().split()

A = list(map(int,A))
B = list(map(int,B))

new_list =[]
new_list.append((A))
new_list.append((B))
final_list= list(product(*new_list))

for i in final_list:
    print(i, end=" ")
