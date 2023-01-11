all_palinNum = []
def isPalindrome(s):
    return s == s[::-1]
for num1 in range(999,100,-1):
    for num2 in range(999,100,-1):
        total = num1 * num2
        if(isPalindrome(str(total))):
            all_palinNum.append(total)
print(max(all_palinNum))