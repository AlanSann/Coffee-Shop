print("\nHello, welcome to BetterHumanity Coffee Shop!\n ")

name = input("What is your name ?\n")

print("Hello " + name+ ", thank you so much for coming in today.\n")

menu =  "Black Coffee, Espresso, Latte, Capuccino"

print(name + ", what would you like to drink today ? Here is what we are serving :\n" + menu )

order = input()

price = 1

quantity = input("\nHow many of these would you like ?\n")

total = price * int(quantity)

print("Sounds good " + name + ", we will have your " + quantity + " " + order + " ready for you in a moment. Your total is : " + str(total) + " €")