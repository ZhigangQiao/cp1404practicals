import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_prices.txt"  # Define the output file name

price = INITIAL_PRICE
day = 0

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

# Print the starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate the stock prices for each day
while MIN_PRICE <= price <= MAX_PRICE:
    # Increment the day count
    day += 1
    price_change = 0
    # 50% chance of increase or decrease
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    # Update the price
    price *= (1 + price_change)
    # Print the price for each day
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()
