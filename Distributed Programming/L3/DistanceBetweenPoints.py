import math

def distance(x1, y1, x2, y2):
    one = x2 - x1
    one = pow(one, 2)
    two = y2 - y1
    two = pow(two, 2)

    return math.sqrt(one + two)


print("Choose the first point")
x11 = int(input("Enter x1: "))
y11 = int(input("Enter y1: "))

print("Choose the second point")
x22 = int(input("Enter x2: "))
y22 = int(input("Enter y2: "))

dst = distance(x11, y11, x22, y22)
print("The distance is:", dst)