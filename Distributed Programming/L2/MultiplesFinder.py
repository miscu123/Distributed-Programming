def multiples_finder():
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))

    if x >= y:
        print("No multiples found")
    else:
        print("Multiples found: ")

    multiple = x
    i = 1
    while multiple < y:
        print(multiple)
        i += 1
        multiple = multiple * i


multiples_finder()