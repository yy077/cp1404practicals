# list_comprehensions.py
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(10) if x % 2 == 0]
uppercase_names = [name.upper() for name in ["alice", "bob", "charlie"]]

print(squares)
print(even_numbers)
print(uppercase_names)