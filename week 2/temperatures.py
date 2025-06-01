def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def main():
    celsius = float(input("Enter Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Result: {fahrenheit:.2f} F")

    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"Result: {celsius:.2f} C")


if __name__ == "__main__":
    main()