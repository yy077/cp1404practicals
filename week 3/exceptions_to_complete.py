is_valid = False
while not is_valid:
    try:
        result = int(input("Enter a valid integer: "))
        is_valid = True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print(f"Valid integer entered: {result}")