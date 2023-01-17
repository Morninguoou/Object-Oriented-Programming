def count_minus(str):
    return len([int(count) for count in str if int(count) < 0])
print(count_minus(input().split())) 