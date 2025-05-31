"""
CP1404/CP5632 - Practical
"""
def main():
    # Input validation loop for number of items
    while True:
        try:
            number_of_items = int(input("Number of items: "))
            if number_of_items < 0:
                print("Invalid number of items!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    total_price = 0

    for i in range(number_of_items):
        while True:
            try:
                price = float(input("Price of item: "))
                if price < 0:
                    print("Price cannot be negative.")
                else:
                    total_price += price
                    break
            except ValueError:
                print("Please enter a valid price.")

    # Apply discount if total is over $100
    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount

    print(f"Total price for {number_of_items} items is ${total_price:.2f}")

if __name__ == '__main__':
    main()

