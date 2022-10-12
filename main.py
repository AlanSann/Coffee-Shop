#from time import sleep


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

print(name + ", what would you like to drink today ? Here is what we are serving :\n" + menu )

order = input()

price = 1

quantity = input("\nHow many of these would you like ?\n")

total = price * int(quantity)

print("Sounds good " + name + ", we will have your " + quantity + " " + order + " ready for you in a moment. Your total is : " + str(total) + " €")
    
#def drink_time():
        #print("\nAre you finished ?")
        
#sleep(5); drink_time()
    
