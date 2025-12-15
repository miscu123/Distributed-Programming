def remove_duplicates(inpt):
    vector = []
    i = 0

    while i < len(inpt):
        sign = 1

        if inpt[i] == '-' and i + 1 < len(inpt) and inpt[i + 1].isdigit():
            sign = -1
            i += 1

        if i < len(inpt) and inpt[i].isdigit():
            number = 0
            while i < len(inpt) and inpt[i].isdigit():
                number = number * 10 + int(inpt[i])
                i += 1
            if number not in vector:
                vector.append(sign * number)
        else:
            i += 1

    print("The list without duplicates:")
    for num in vector:
        print(num)


inp = input("Enter the numbers separated by a ',': ")
remove_duplicates(inp)