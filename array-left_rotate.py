inp = list(map(int, input().split()))
arr = []

for i in range(inp[0]):
    arr.append(i+1)

for i in range(inp[1]):
    newarr1 = arr[1:]
    newarr2 = arr[0]
    newarr1.append(newarr2)
    arr = newarr1
    print(arr)


print("The final rotated array is {}".format(arr))



