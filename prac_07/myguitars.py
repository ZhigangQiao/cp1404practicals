from guitar import Guitar


def load_guitars(file_name):
    guitars = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        print("File not found. No existing guitars loaded.")
    return guitars


def display_guitars(guitars):
    for index, guitar in enumerate(guitars, 1):
        print(f"Guitar {index}: {guitar}")


def add_guitar():
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year the guitar was made: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)


def write_guitars(guitars, file_name):
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}\n")


def main():
    file_name = 'guitars.csv'
    guitars = load_guitars(file_name)
    print("Loaded Guitars:")
    display_guitars(guitars)

    new_guitar = add_guitar()
    guitars.append(new_guitar)
    print("\nAdded New Guitar:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted Guitars:")
    display_guitars(guitars)

    write_guitars(guitars, file_name)
    print("\nGuitars saved to file.")


if __name__ == '__main__':
    main()
