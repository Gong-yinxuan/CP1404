PASSWORD_LENGTH = 10




def validate_password():
    password = input("Enter your password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Enter your password: ")

    return password