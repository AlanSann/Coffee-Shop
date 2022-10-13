from time import sleep


# Creating my scenario 

print("\nHello, welcome to BetterHumanity Coffee Shop!\n ")

name = input("What is your name ?\n")

# If, Elif, Else statements to play with 

if name == "Ben" or name == "Patricia" :
    evil_status = input("Are you evil ?\n")
    if evil_status == "Yes" :
        print("Get the fuck out of here!") 
        exit()
    elif evil_status == "No" : 
        print("Oh so you are one of those good Ben, Hello " + name + ", thank you so much for coming in today.\n")
else :
    print("Hello " + name + ", thank you so much for coming in today.\n")
    
# Creating a list for our menu can be really usefull but we just could have declared a str variable if our menu remains like this

menu =  ["Black Coffee", "Espresso", "Latte", "Capuccino", "Frappuccino"]

order = input(name + ", what would you like to drink today ? Here is what we are serving :\n" + str(menu) +"\n" )

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
    
# Creating a delay time method that prints this sentence 5 seconds after the previous action

def drink_time():
        end_coffee = input("\nAre you finished ?")
        
sleep(5); drink_time()


    
