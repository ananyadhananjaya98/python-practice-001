arr = []

for i in range(6):
     arr.append(list(map(int, input().split())))

final_sum = []
sum1 = 0
for i in range(4):
     for j in range(4):
       sum1 += arr[i][j]+arr[i][j+1]+arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
       final_sum.append(sum1)
       sum1 = 0

print(max(final_sum))
