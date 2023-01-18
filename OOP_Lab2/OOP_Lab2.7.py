dayInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(y):
    if y % 400 == 0:
        return 1
    elif y % 100 != 0 and y%4 == 0:
        return 1
    else:
        return 0
def day_of_year(d,m,y):
    sum = 0
    if is_leap(y):
        dayInMonth[2] = 29
    for i in range(m):
        sum+=dayInMonth[i]
    sum += d
    return sum 