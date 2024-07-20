
upper_case = 0
lower_case = 0

def char_count(str1):
    for c in str1:
        if c is c.upper:
            upper_case += 1
        elif c is c.lower:
            lower_case += 1
    
    return upper_case, lower_case

str1 = input("Enter a string of your choice")
upper_case, lower_case = char_count(str1)

print(f"The number of lower case letters is {lower_case}. \nThe number of upper case letters is {upper_case}.")