def maximum_minimum(inpt):
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
            vector.append(sign * number)
        else:
            i += 1

    print("Converted to a list:")
    for num in vector:
        print(num)

    if vector:
        print("Maximum number:", max(vector))
        print("Minimum number:", min(vector))


inp = input("Enter the numbers separated by a ',': ")
maximum_minimum(inp)
