def tuple_search(inpt, srch):
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

    my_tuple = tuple(vector)
    if srch in my_tuple:
        print(srch, "is found in tuple at index:", my_tuple.index(srch))
    else:
        print(srch, "is not found in tuple")


inp = input("Enter the numbers separated by a ',': ")
src = int(input("Search for: "))
tuple_search(inp, src)