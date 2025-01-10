#A function that takes a number as input and returns the factorial of that number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number"))
print(f"The factorial of {n} is {factorial(n)}")