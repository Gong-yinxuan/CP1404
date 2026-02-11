"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects_info = load_data(FILENAME)
    print(subjects_info)
    print_data(subjects_info)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)

    subjects_list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts

        data = [parts[0], parts[1], int(parts[2])]
        subjects_list.append(data)
    input_file.close()
    return subjects_list

def print_data(subjects_info):
    for data in subjects_info:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students.")

main()