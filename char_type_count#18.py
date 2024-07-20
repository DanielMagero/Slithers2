def chartype_count(str):
    lower_case = 0
    upper_case = 0
    spec_char = 0
    num_char = 0

    for char in str:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
        elif char.isdigit():
            num_char += 1
        else:
            spec_char += 1
    return lower_case, upper_case, spec_char, num_char

str = input("Enter a string containing different types of characters: ")
lower_case, upper_case, spec_char, num_char = chartype_count(str)
print(f"Lowercase: {lower_case} \nUppercase: {upper_case} \nSpecial characters: {spec_char} \nNumeric characters: {num_char}")