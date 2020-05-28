n,m = map(int, input().split())

array = set((input().split()))

Alike = set(input().split())
Bdislike = set(input().split())

happiness = 0

for i in array:
    if i in Alike:
        happiness+=1
    if i in Bdislike:
        happiness-=1

print(happiness)

