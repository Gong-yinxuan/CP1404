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

# 3.
with open("numbers.txt", "r") as in_file:
    first_line = in_file.readline()
    second_line = in_file.readline()

num1 = int(first_line)
num2 = int(second_line)
sum = num1 + num2
print(sum)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)

print(total)