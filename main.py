from member import member, premium_member
from product import book, cd, game
from member_id import create_member_id

Matt = member("Matt", "Mango")
Jeff = premium_member("Jeff", "Dickson", True)
hive = book("The Hive", 8.99, 10, "Orson Scott Card")
tswift = cd("Lover", 11.99, 29, "Taylor Swift")
ratchet = game("Ratchet and Clank", 49.99, 7, "PS2")
inventory = [hive, tswift, ratchet]
members = [Matt]
premium_members = [Jeff]


def welcome():
    print("Welcome to the Bookstore! \n" +"Select one: \n" +
          "1. See inventory \n" + "2. New member \n"  + "3. Show Inventory")
    screen_1 = input()
    
    if screen_1 == "1":
        for n in inventory:
            print(n.name + " $" +  str(n.price) + " " +str(n.inventory) + " in stock")
    elif screen_1 == "2":
        new_user()
    elif screen_1 == "3":
        print_Inventory()

def new_user():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    premium = input("Would you like to be a premium member? Y/N ")

    if premium == "Y" or "y" or "yes" or "1":
        new_member = member(first_name, last_name)
        members.append(new_member)
    if premium == "N" or "n" or "no" or "0":
        new_member = premium_member(first_name, last_name, True)
        premium_members.append(new_member)
    else:
        print("Please enter either 1 or 2.")
        new_user()

    print(new_member.first_name + " " + new_member.last_name + ", you are all signed up!\n")

    welcome()

def print_Inventory():
    for n in inventory:
        print(str(n.name) + ", $" + str(n.price) + ", " + str(n.inventory) + " available")


welcome()
