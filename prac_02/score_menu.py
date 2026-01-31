def main():

    menu = """Menu:
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""

    choice = ""

    while choice != "Q":
        print(menu)
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()



def get_valid_score():
    score = float(input("Enter a score(0-100): "))

    while score < 0 or score > 100:
        score = float(input("Enter a score(0-100): "))
        print("Score must be between 0 and 100.")

    return score