"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random
def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(f"User score {score} is {result}")

    if result == "Excellent":
        print("Excellent")

    random_score = random.randint(0, 100)
    random_result = check_score(random_score)
    print(f"Random: {random_score} = {random_result}")


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
