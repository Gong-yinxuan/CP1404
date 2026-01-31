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

