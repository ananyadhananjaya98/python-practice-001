N = int(input())
strings = []
queries = []
results = []

for i in range(N):
    strings.append(input())

Q = int(input())

for i in range(Q):
    queries.append(input())

for i in queries:
    count = 0
    for j in range(N):
        if i == strings[j]:
            count+=1
    results.append(count)

print(results)
