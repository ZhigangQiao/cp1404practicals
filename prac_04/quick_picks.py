import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PICKS = 6


def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_PICKS))


def display_quick_picks(num_picks):
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2d}" for number in quick_pick))


def main():
    num_picks = int(input("How many quick picks? "))
    display_quick_picks(num_picks)


if __name__ == "__main__":
    main()
