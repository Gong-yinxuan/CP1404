def main():
    email_to_name = {}

    email = input("Email: ")
    while email.strip() != '':
        name = extract_name(email)

        confirm = input(f"Is your name {name}? (Y/n): ")
        if confirm.lower() == "n" or confirm.lower() == "no":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    name_parts = email.split("@")[0]
    parts = name_parts.split(".")
    name = " ".join(parts).title()  # 用空格联系两个部分，首字母大写
    return name

main()


