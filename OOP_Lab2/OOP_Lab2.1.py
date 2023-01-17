num = input().split()
num = list(map(int,num))
num = sorted(num)
check = 0
ans = 1
for i in range(len(num)): #check 0
    if num[i] == 0:
        check +=1
    else: continue

if check > 0: #multiple 10 ans del 0
    if check == 1:
        ans *= 10
        ans*=num[check]
        del num[1]
    else:
        for n in range(check):
            ans *= 10
        ans*=num[check]
        for x in range(check):
            del num[x]

if check > 0: #have 0
    for i in range(len(num)):
        if i == 0:
            ans += num[i]
        else:
            ans = (ans*10)+num[i]
elif check == 0:
    for i in range(len(num)):
        if i == 0:
            ans *= num[i]
        else:
            ans = (ans*10)+num[i]

print(ans)