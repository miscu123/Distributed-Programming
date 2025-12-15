def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))
result = factorial(number)

if result == 0:
    print("Negative numbers do not have factorials!")
else:
    print("Factorial of", number, "is:", result)