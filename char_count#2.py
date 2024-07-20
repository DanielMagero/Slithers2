def count_char(chat):
    dic_count = {}
    for char in chat:
        if char in dic_count:
            dic_count[char] += 1
        else:
            dic_count[char] = 1
    return dic_count

string = input("Enter a word of your choice:")
str_count = count_char(string)
print(str_count)