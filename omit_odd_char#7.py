def omit(str1):
    final_str = ''.join([char for index, char in enumerate(str1) if index % 2 == 0])
    return final_str

print("Removing odd positioned letters from a word.")
str1 = input("Enter a word of your choice:")
print(omit(str1))