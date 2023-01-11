x = input("")
Up = 0
Low = 0
for i in range(len(x)):
    if x[i].isupper():
        Up+=1
    elif x[i].islower():
        Low+=1
print('Uppercase letters :',+Up)
print('Lowercase letters :',+Low)