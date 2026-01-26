"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

"""
Test:
score = -20
output = Invalid score

score = 101
output = Invalid score

score = 0 
output = bad

score = 100
output = Excellent

score = 35
output = bad

score = 50
output = passable

score = 66
output = passable

score = 90
output = Excellent

score = 99
output = Excellent
"""