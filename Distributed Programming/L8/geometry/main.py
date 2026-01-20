import circle
import rectangle

def main():
    radius = float(input("Introduceti raza cercului: "))
    if radius < 0:
        print("Raza nu poate fii negativa.")
        return

    area = circle.calc_area(radius)
    circumference = circle.calc_circumference(radius)
    print(f"Aria cercului: {area:.2f}")
    print(f"Circumferinta cercului: {circumference:.2f}")

    length = float(input("Introduceti lungimea dreptunghiului: "))
    width = float(input("Introduceti latimea dreptunghiului: "))

    if length < 0 or width < 0:
        print("Lungime / latime nu pot fii negative.")
        return

    area = rectangle.calc_area(length, width)
    perimeter = rectangle.calc_perimeter(length, width)
    print(f"Aria dreptunghiului: {area:.2f}")
    print(f"Perimetrul dreptunghiului: {perimeter:.2f}")

if __name__ == '__main__':
    main()