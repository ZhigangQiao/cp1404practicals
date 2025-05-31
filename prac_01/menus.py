"""
CP1404/CP5632 - Practical
"""

name = input("Enter name: ")

while True:
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = input(">>> ").upper()

    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    elif choice == "Q":
        print("Finished.")
        break
    else:
        print("Invalid choice")
