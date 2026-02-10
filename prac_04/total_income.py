"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of month_count."""
    incomes = []
    month_count = int(input("How many month_count? "))

    for month in range(1, month_count + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)
    print_incomes(month_count, incomes)

def print_incomes(month_count, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_count + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month{month: 2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()