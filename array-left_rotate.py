inp = list(map(int, input().split()))
arr = []

for i in range(inp[0]):
    arr.append(i+1)

newarr =arr
for i in range(inp[1]):
    newarr1 = arr[i:]
    newarr2 = arr[:i]
    newarr1.extend(newarr2)
    arr =newarr1
    print(arr)
    newarr.clear()

print("The final rotated array is {}".format(arr))

