def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it is prime: "))
print(prime_number(num))