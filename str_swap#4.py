def swap(str1, str2):

    str1_new = str1[:2] + str2[2:]
    str2_new = str2[:2] + str1[2:]

    final_str = str1_new + " " + str2_new
    return final_str

print("Enter two words that are more than three letter long.")
str1 = input("Enter your first word: ")
str2 = input("Enter your second word:")

final_str = swap(str1, str2)

print(final_str)
