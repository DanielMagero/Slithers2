#MUGULO DANIEL MAGERO M24B38/017
#PYTHON FUNCTIONS

#2
#function to sum numbers in a string
def sum_list(lst):
    return sum(lst)

lst = [8, 2, 3, 0, 7]
print(sum_list(lst))



#4
#function to reverse any string
def reverse(str1):
    return str1[::-1]

str1 = input("Enter a string of your choice: ")
print(reverse(str1))



#5
#function to get the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    

number = int(input("Enter a number of your choice to get it's factorial: "))
print(factorial(number))



#8
#creates a new list with unique characters from a list with repeated ones
def new_list(lst1):
    return list(set(lst1))

lst1 = [1, 2, 3, 3, 3, 3, 4, 5]
print(new_list(lst1))



#9
#function to check for prime numbers
def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it is prime: "))
print(prime_number(num))



