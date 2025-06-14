def get_income_input(month):
    """Get income input for a specific month using an f-string."""
    return float(input(f"Enter income for month {month}: "))


def print_income_report(month_incomes):
    """Print income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(month_incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = get_income_input(month)
        incomes.append(income)

    print_income_report(incomes)


main()

# Changes made:

# Used an f-string for getting the income input to enhance readability and simplicity.

# Refactored the variable months to num_months for clarity, making it more descriptive and easier to understand.

# Moved the report printing functionality to its own function print_income_report to adhere to the Single
# Responsibility Principle (SRP). This function only accepts the list of month incomes as input.

# Used enumerate to iterate through the months and incomes simultaneously, avoiding indexing errors and improving
# code readability.
