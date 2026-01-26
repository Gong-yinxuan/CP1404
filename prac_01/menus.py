name = input("Enter name: ")
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = input(">>>").upper()
while choice != "Q":
    print(menu)
    choice = input(">>>").upper()
