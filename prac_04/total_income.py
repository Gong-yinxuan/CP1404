"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    month_count = int(input("How many month_count? "))
    incomes = get_incomes(month_count)
    print_incomes(month_count, incomes)

def get_incomes(month_count):
    incomes = []
    for month in range(1, month_count + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)
    return incomes

def print_incomes(month_count, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_count + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month{month: 2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()