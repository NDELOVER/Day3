print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age <= 12 :
        bill = 5
        print("Child tickets are 5$.")
    elif age <= 18:
        bill = 7
        print ("Youth tickets are 7$.")
    elif 45 < age <=55:
        print("your ticket is free.")
    else:
        bill = 12
        print("Adult tickets are 12$.")
    photo = input("Do you want to take a photo? ")
    if photo == "y" or photo == "Y":
        bill += 3
    print(f"Your final bill would be {bill}$")
else:
    print("Sorry you have to grow taller before you can ride.")