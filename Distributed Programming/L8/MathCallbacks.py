import math

def square_root(num):
    return math.sqrt(num)

def factorial(num):
    return math.factorial(num)

def sinus(angle):
    return math.sin(angle)

def main():
    number = input("Introduceti un nr: ")
    angl = input("Introduceti un unghi: ")
    print("Radacina patrata: ", square_root(int(number)))
    print("Factorial: ", factorial(int(number)))
    print("Sinus: ", sinus(int(angl)))

if __name__ == '__main__':
    main()