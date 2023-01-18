def count_minus(str):
    return len([int(count) for count in str.split() if int(count) < 0])