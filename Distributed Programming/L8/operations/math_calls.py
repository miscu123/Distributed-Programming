import math_operations

def main():
    a = int(input("Introduceti nr1: "))
    b = int(input("Introduceti nr2: "))
    print("Adunare: ", math_operations.add(a, b))
    print("Scadere: ", math_operations.diff(a, b))
    print("Inmultire: ", math_operations.mul(a, b))
    print("Impartire: ", math_operations.div(a, b))

if __name__ == "__main__":
    main()