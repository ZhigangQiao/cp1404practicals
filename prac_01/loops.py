"""
CP1404/CP5632 - Practical
"""

# a. Count in 10s from 0 to 100
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

# b. Count down from 20 to 1
print("b. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

# c. Print n stars
print("c. Print n stars:")
num_stars = int(input("Number of stars: "))
for i in range(num_stars):
    print('*', end='')
print("\n")

# d. Print n lines of increasing stars
print("d. Print n lines of increasing stars:")
num_stars = int(input("Number of stars: "))
for i in range(1, num_stars + 1):
    print('*' * i)
