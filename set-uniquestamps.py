n = int(input())
totalstamps= []

for i in range(n):
    totalstamps.append(input())

print(len(set(totalstamps)))
