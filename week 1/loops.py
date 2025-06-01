"""""
Display "Odd numbers from 1 to 20:"
For i from 1 to 20, step by 2
    Display i, separated by a space
Display a newline

Display "Count in 10s from 0 to 100:"
For i from 0 to 100, step by 10
    Display i, separated by a space
Display a newline

Display "Count down from 20 to 1:"
For i from 20 to 1, step by -1
    Display i, separated by a space
Display a newline

Display "Print n stars:"
Get n
For i from 1 to n
    Display "*"
Display a newline

Display "Print n lines of increasing stars:"
Get n
For i from 1 to n
    For j from 1 to i
        Display "*"
    Display a newline
"""
print("Odd numbers from 1 to 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()


print("\nCount in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print("\nCount down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print("\nPrint n stars:")
n = int(input("Number of stars: "))
for _ in range(n):
    print("*", end='')
print()

print("\nPrint n lines of increasing stars:")
for i in range(1, n + 1):
    print("*" * i)