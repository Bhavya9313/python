menu = {
    "pizza":40,
    "pasta":60,
    "burger":60,
    "salad":50,
    "coffee":80
}

print("welcome to PYTJON RESTAURANT")
print("pizza: rs40\n pasta: rs60\n burger: rs60\n salad: 50\n coffee: 80\n")

order_total = 0
item1 = input("enter the name of item you want to order = ").lower()
if item1 in menu:
    n = int(input("how much item you want"))
    order_total += n*(menu[item1])
    print(f"ordered item {item1} has been added to your order")
else:
    print(f"ordered item {item1} is not abailable yet!")

while True:
    another_order = input(f"do you want to add another item?(yes/no)")
    if another_order == "yes":
        item2 = input("enter the name of next item = ").lower()
        if item2 in menu:
            order_total +=menu[item2]
            print(f"item {item2} has been added to your order")

        else:
            print("f ordered item {item2} is not abailable yet!")
            break
    else:
        break
print(f"total amount of item is {order_total}")