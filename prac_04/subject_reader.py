"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    print(data)
    print_data(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)

    all_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts

        data = [parts[0], parts[1], int(parts[2])]
        all_data.append(data)
    input_file.close()
    return all_data

def print_data(all_data):
    for data in all_data:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students.")

main()