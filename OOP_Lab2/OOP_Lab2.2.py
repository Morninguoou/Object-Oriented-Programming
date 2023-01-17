def count_char_in_string(x,c):
    return [char.count(c) for char in x]
print(count_char_in_string(input().split(),input()))