# 1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2.
in_file = open("name.txt", "r")
content = in_file.read()
in_file.close()
print(f"Hi {content}!")