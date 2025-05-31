def main():
    print("Welcome to the Score Program!")

    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print("Result:", determine_score_status(score))
        elif choice == "S":
            print("Stars:")
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using the Score Program! Goodbye!")
            break
        else:
            print("Invalid input. Please enter G, P, S, or Q.")

def get_valid_score():
    """
    Get a valid score from the user (0-100 inclusive).
    """
    while True:
        score = float(input("Enter score (0-100): "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Score must be between 0 and 100 inclusive.")

def determine_score_status(score):
    """
    Determine the status of the score.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """
    Print stars equal to the score.
    """
    print("*" * int(score))

if __name__ == "__main__":
    main()
