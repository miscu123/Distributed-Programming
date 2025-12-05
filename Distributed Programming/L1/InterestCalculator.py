def interest_calculator():
    principal = input("Enter principal: ")
    rate = input("Enter rate: ")
    time = input("Enter time: ")

    interest = (float(principal) * float(rate) * float(time)) / 100
    print("The interest is: ", interest)


interest_calculator()