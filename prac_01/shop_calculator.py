item_num=int(input("Enter the number of item: "))
sum_price = 0
for i in range(1,item_num+1):
    price = float(input(f"Enter the price of item {i}: "))
    sum_price += price