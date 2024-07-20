def digit_sum(str):
    sum_dig = 0
    for char in str:
        if char.isdigit():
            sum_dig += int(char)
    return sum_dig

str = input("Enter a string with numbers in it: ")
print(digit_sum(str))