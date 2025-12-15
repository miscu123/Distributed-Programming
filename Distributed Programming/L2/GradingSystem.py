def grading():
    score = int(input("Enter score: "))
    print("Grade: ")

    if 90 <= score < 101:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    elif score > 100:
        print("Error")
    else:
        print("F")


grading()
