"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # Ensure that we have exactly three parts in each line
        if len(parts) != 3:
            print(f"Skipping line due to incorrect format: {line}")
            continue
        subject_code, lecturer, student_count = parts
        try:
            student_count = int(student_count)  # Convert the student count to an integer
        except ValueError:
            print(f"Error: Unable to convert student count '{student_count}' to an integer.")
            continue  # Skip this line if conversion fails
        data.append([subject_code, lecturer, student_count])  # Append the processed parts to the data list
    input_file.close()
    return data  # Return the list of lists


def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


def main():
    data = get_data()
    display_subject_details(data)


if __name__ == "__main__":
    main()
