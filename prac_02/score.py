import random

def main():
    user_score = float(input("Enter score: "))
    print(determine_score_status(user_score))

    random_score = random.randint(0, 100)  # Generate a random score between 0 and 100
    print("Random score:", random_score)
    print(determine_score_status(random_score))

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


if __name__ == "__main__":
    main()
