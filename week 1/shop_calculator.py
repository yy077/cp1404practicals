"""""
Display "Number of items:"
Get number_of_items
While number_of_items < 0
    Display "Invalid number of items!"
    Display "Number of items:"
    Get number_of_items
Initialize total_price = 0
For i from 1 to number_of_items
    Display "Price of item:"
    Get price
    total_price = total_price + price
If total_price > 100
    total_price = total_price * 0.9
Display "Total price for ", number_of_items, " items is $" and total_price
"""
def main():
    total_price = 0
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    for _ in range(number_of_items):
        price = float(input("Price of item: "))
        total_price += price
    if total_price > 100:
        total_price *= 0.9
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")

main()