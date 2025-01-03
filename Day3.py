height = int(input("Please enter your height: "))

if height >= 120:
    age = int(input("Please enter your age: "))
    photo = input("Do you want a photo? Y or N")
    cost = 0
    if photo == "Y":
        print("You can ride.")
        if age < 12 :
            cost = 5 + 3
            print(f"You have to pay {cost}$")
        elif 12 <= age <= 18:
            cost = 7 + 3
            print(f"You have to pay {cost}$")
        else:
            cost = 12 + 3
            print(f"You have to pay {cost}$.")
    elif photo == "N":
        print("You can ride.")
        if age < 12:
            cost = 5
            print(f"You have to pay {cost}$")
        elif 12 <= age <= 18:
            cost = 7
            print(f"You have to pay {cost}$")
        else:
            cost = 12
            print(f"You have to pay {cost}$.")
else:
    print("You can't ride.")