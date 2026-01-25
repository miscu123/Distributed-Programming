def celsius_fahrenheit():
    temperature = input("Enter the temperature in Celsius: ")
    if not temperature.isdigit():
        raise TypeError("Temperature must be a number")
    else:
        temperature = float(temperature)
        print("Temperature in Fahrenheit: ", temperature * 9/5 + 32)


celsius_fahrenheit()