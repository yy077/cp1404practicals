name = input("Enter your name: ")
with open("name.txt", "w") as f:
    f.write(name)

with open("name.txt", "r") as f:
    name = f.read()
print(f"Hi {name}!")

with open("numbers.txt", "r") as f:
    first_number = int(f.readline())
    second_number = int(f.readline())
print(first_number + second_number)

total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line)
print(total)