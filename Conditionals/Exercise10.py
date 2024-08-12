#Bella Napoli pizzeria offers vegetarian and non-vegetarian pizzas to its customers. 
# The ingredients for each type of pizza appear below.

#Vegetarian ingredients: Pepper and tofu.
#Non-vegetarian ingredients: Pepperoni, Ham and Salmon.
#Write a program that asks the user if they want a vegetarian pizza or not, and based on their answer, 
# shows them a menu with the ingredients available for them to choose from. You can only choose
#  one ingredient besides the mozzarella and tomato that are on all pizzas. At the end it must be 
# shown on the screen whether the chosen pizza is vegetarian or not and all the ingredients it contains.


type=input("Introduce V for a vegetarian pizza and N for a not vegetarian one: " )

if(type=="V"):
    print("Choose the extra ingredients for your vegetarian pizza: ")
    extraV=input("P for pepper or T for tofu: ")
    if(extraV=="P"):
        print("Your pizza is vegetarian and the ingredients of your pizza are: Mozzarella, tomato and pepper")
    elif(extraV=="T"):
        print("Your pizza is vegetarian and the ingredients of your pizza are: Mozzarella, tomato and tofu")
    else:
        print("You didnt choose a correct ingredient")
elif(type=="N"):
    print("Choose the extra ingredients for your not vegetarian pizza: ")
    extraV=input("P for pepperoni, H for ham and S for Salmon")
    if(extraV=="P"):
        print("Your pizza is not vegetarian and the ingredients of your pizza are: Mozzarella, tomato and pepperoni")
    elif(extraV=="H"):
        print("Your pizza is not vegetarian and the ingredients of your pizza are: Mozzarella, tomato and ham")
    elif(extraV=="S"):
        print("Your pizza is not vegetarian and the ingredients of your pizza are: Mozzarella, tomato and salmon")
    else:
        print("You didnt choose a correct ingredient")
else:
    print("You didnt choose a correct pizza option")
