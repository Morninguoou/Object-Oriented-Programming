def delete_minus(x):
    return [[two for two in one if two >= 0] for one in x]

print(delete_minus([ [1, -3, 2], [-8, 5], [-1, -4, -3] ]))
# def count_char_in_string(x,c):
#     return [char.count(c) for char in x]
# print(count_char_in_string(input().split(),input()))