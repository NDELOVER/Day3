size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
# extra_cheese = input("Do you want extra cheese? Y or N:")
bill = 0
if size == "s" or size == "S":
    bill = 15
    print("15$")
elif size == "m" or size == "M":
    bill = 20
    print("20$")
elif size == "l" or size == "L":
    bill = 25
    print("25$")
add_extra_pepperoni = input("Do you want extra pepperoni? Y or N? ")
add_extra_cheese = input("Do you want extra cheese? Y or N? ")
if add_extra_pepperoni == "y" or add_extra_pepperoni == "Y" and size == "s" or size == "S":
    bill += 2
elif add_extra_pepperoni == "y" or add_extra_pepperoni == "Y" and size == "m" or size == "M" or size == "l" or size == "L":
    bill += 3
if add_extra_cheese == "y" or add_extra_cheese == "Y":
    bill+=1
print(f"your final order would be {bill}$")
