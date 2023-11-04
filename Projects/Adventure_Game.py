name = input("Type your name: ")

print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go" +
                " left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk or swim: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died. You lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. " +
                    "Do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You head back but on your way die. You lose")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. " + 
                        "Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended so you lose")
        else:
            print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name)
