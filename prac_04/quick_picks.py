import random
picks_num = int(input("How many 'quick picks' would you like to generate? "))
for row in range(picks_num):
    for col in range(0,6):
        number = random.randint(1, 45)
        print(number, end=" ")
    print(end="\n")
