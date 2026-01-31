def main():
    menu = """Menu:
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""

    choice = ""
    score = None

    while choice != "Q":
        print(menu)
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()

        elif choice == "P":

            if score is not None:
                result = check_score(score)
                print(f"Score {score} is {result}")
            else:
                print("No score entered yet. Please get a valid score first.")

        elif choice == "S":
            if score is not None:
                show_stars(score)
            else:
                print("No score entered yet. Please get a valid score")


def get_valid_score():
    score = float(input("Enter a score(0-100): "))

    while score < 0 or score > 100:
        score = float(input("Enter a score(0-100): "))
        print("Score must be between 0 and 100.")

    return score

def check_score(score):
    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
        stars = "*" * int(score)
        print(stars)

