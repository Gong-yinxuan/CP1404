PASSWORD_LENGTH = 10

password = input("Enter your password: ")
while len(password) < PASSWORD_LENGTH:
    print("Invalid password")
    password = input("Enter your password: ")

print(len(password) * "*")