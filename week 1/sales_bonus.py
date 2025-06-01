"""""
Display "Enter sales: $"
Get sales
While sales >= 0
    If sales < 1000
        Calculate bonus = sales * 0.1
    Else
        Calculate bonus = sales * 0.15
    Display "Bonus: $" and bonus
    Display "Enter sales: $"
    Get sales
Display "Thank you."
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))