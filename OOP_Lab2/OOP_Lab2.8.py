dayInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(y):
    if y % 400 == 0:
        return 1
    elif y % 100 != 0 and y % 4 == 0:
        return 1
    else:
        return 0

def day_of_year(d,m,y):
    dayInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    if is_leap(y) == 1:
        dayInMonth[2] = 29
    for i in range(m):
        sum+=dayInMonth[i]
    sum += d
    return sum

def day_in_year(y):
    if is_leap(y):
        return 366
    else: return 365

def date_diff(first,second):
    first_list = [int(n) for n in first.split("-")]
    second_list = [int(n) for n in second.split("-")]
    totalDay = 0
    for i in range(first_list[2], second_list[2]):
        totalDay += day_in_year(i)
    totalDay -= day_of_year(first_list[0], first_list[1], first_list[2])
    totalDay += day_of_year(second_list[0], second_list[1], second_list[2])
    totalDay+=1

    return totalDay