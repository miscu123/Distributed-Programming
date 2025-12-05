def is_prime():
    number = int(input("Enter a number: "))
    div_count = 0

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            div_count += 1

    if div_count > 0:
        print("The number is NOT prime.")
    else:
        print("The number is prime.")


is_prime()