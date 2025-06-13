# total_income.py

def get_income_report():
    num_months = int(input("How many months? "))
    incomes = []

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    print("\nIncome Report")
    print("-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:8.2f}         Total: ${total:8.2f}")



get_income_report()