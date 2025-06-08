import random

# What did you see on line 1?
# - A random integer between 5 and 20, inclusive.

# What was the smallest number you could have seen, what was the largest?
# - Smallest: 5
# - Largest: 20

print(random.randint(5, 20))  # line 1

# What did you see on line 2?
# - A random odd integer between 3 and 9, inclusive.

# What was the smallest number you could have seen, what was the largest?
# - Smallest: 3
# - Largest: 9

# Could line 2 have produced a 4?
# - No, because the step is 2, so only odd numbers will be produced.

print(random.randrange(3, 10, 2))  # line 2

# What did you see on line 3?
# - A random floating-point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# - Smallest: 2.5
# - Largest: 5.5

print(random.uniform(2.5, 5.5))  # line 3

# Write code to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
