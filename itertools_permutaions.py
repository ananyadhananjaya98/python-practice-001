from itertools import permutations

input1 = input().split()
string = input1[0]
r = int(input1[1])
list01 = (list(permutations(string,r)))

final_list01 = list(sorted(list01))

final_list = list(map(list, final_list01))
print(final_list)
new =[]
for i in final_list:
    new.append(''.join(i))
for i in new:
    print(i)

