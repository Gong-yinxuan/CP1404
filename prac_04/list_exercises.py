print("Please enter 5 numbers: ")
numbers = []
for i in range(0,5):
    number = int(input(f"enter number {i+1}:"))
    print(f"Number: {number}")
    numbers.append(number)

print(f"The first number is: {numbers[0]}")
print(f"The last number is: {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The average number is: {sum(numbers)/len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")