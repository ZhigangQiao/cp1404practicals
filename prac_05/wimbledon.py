import csv


def read_wimbledon_data(filename):
    """Reads Wimbledon data from a CSV file."""
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            wimbledon_data.append(row)
    return wimbledon_data


def count_champions(wimbledon_data):
    """Counts the number of wins for each champion."""
    champions = {}
    for row in wimbledon_data:
        champion = row[2]  # Index 2 contains champion name
        champions[champion] = champions.get(champion, 0) + 1
    return champions


def list_countries(wimbledon_data):
    """Creates a set of countries of champions."""
    countries = set()
    for row in wimbledon_data:
        countries.add(row[1])  # Index 1 contains country of champion
    return sorted(countries)


def display_champions(champions):
    """Displays champions and their wins."""
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")


def display_countries(countries):
    """Displays countries of champions."""
    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)


def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_wimbledon_data(filename)
    champions = count_champions(wimbledon_data)
    display_champions(champions)
    countries = list_countries(wimbledon_data)
    display_countries(countries)


if __name__ == "__main__":
    main()
