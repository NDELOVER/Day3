height = int(input("Please enter your height: "))

if height >= 120:
    age = int(input("Please enter your age: "))
    print("You can ride.")
    if age > 18 :
        print("You have to pay 12$")
    elif 12 < age <= 18:
        print("You have to pay 7$")
    else:
        print("You have to pay 5$.")
else:
    print("You can't ride.")