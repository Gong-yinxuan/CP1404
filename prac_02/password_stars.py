PASSWORD_LENGTH = 10

def main():
    password = validate_password()
    print(len(password) * "*")


def validate_password():
    password = input("Enter your password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Enter your password: ")

    return password
main()