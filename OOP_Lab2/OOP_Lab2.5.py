def only_english(string1):
    return "".join([char for char in string1 if((char>='a' and char<='z') or (char>='A' and char<='Z'))])
print(only_english(input()))