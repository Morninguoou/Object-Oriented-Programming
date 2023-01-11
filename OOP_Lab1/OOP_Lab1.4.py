number = int(input())
sum = 0
total = 0
temp = number
num_arr = []
for i in range(4):
    sum += temp
    temp *= 10
    num_arr.append(sum)
for i in range(4):
    total +=num_arr[i]
print(total)