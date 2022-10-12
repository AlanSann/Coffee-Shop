from time import sleep


print("\nHello, welcome to BetterHumanity Coffee Shop!\n ")

name = input("What is your name ?\n")

if name == "Ben" :
    evil_status = input("Are you evil ?\n")
    if evil_status == "Yes":
        print("Get the fuck out of here!") 
        exit()
    elif evil_status == "No" : 
        print("Oh so you are one of those good Ben, Hello " + name + ", thank you so much for coming in today.\n")
else :
    print("Hello " + name + ", thank you so much for coming in today.\n")

menu =  "Black Coffee, Espresso, Latte, Capuccino, Frappuccino"

order = input(name + ", what would you like to drink today ? Here is what we are serving :\n" + menu +"\n" )

if order == "Black Coffee":
    price = 1
elif order == "Espresso":
    price = 1.20
elif order == "Latte":
    whipped_cream = input("Do you want whipped cream ?\n")
    if whipped_cream == "Yes" : 
        price = 7.50
    elif whipped_cream == "No" : 
        price = 6.50
elif order == "Capuccino":
    price = 2
elif order == "Frappuccino":
    price = 10
else :
    print("Sorry, we don't have that here.")
    price = 0
    exit()
    
quantity = input("\nHow many of these would you like ?\n")

total = price * int(quantity)

print("Sounds good " + name + ", we will have your " + quantity + " " + order + " ready for you in a moment. Your total is : " + str(total) + " €")
    
def drink_time():
        print("\nAre you finished ?")
        
sleep(5); drink_time()
    
