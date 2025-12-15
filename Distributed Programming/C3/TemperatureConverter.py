def convert_temperature(value, a, b):
    if a == 'C' and b == 'F':
        return value * 9/5 + 32
    elif a == 'C' and b == 'K':
        return value + 273.15
    elif a == 'F' and b == 'C':
        return 5/9 * (value - 32)
    elif a == 'F' and b == 'K':
        return (value + 459.67) * 5/9
    elif a == 'K' and b == 'C':
        return value - 273.15
    elif a == 'K' and b == 'F':
        return (value - 273.15) * 9/5 + 32

    return None


value = float(input('Enter temperature value: '))
a = input('Enter temperature a: ')
b = input('Enter temperature b: ')

temp = convert_temperature(value, a, b)
print("Temperature converted is: ", temp)