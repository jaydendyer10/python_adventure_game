answer = input("Hello, Would you like to play? (yes/no) ")

if answer .lower() .strip() == "yes":

    answer = input(
        "You're walking and reach a fork in the road, would you like to go left or right?").lower().strip()
    if answer == "left":
        answer = input(
            "You encounter a group of zombies, would you like to run or attack?")

        if answer == "attack":
            print("That was a bad idea, you're all alone. Game over")
        else:
            print("Good choice, you ran away and escaped from the zombies")

            answer = input(
                "You run over a hill and see a car and a helicopter, which one would you like to take?")

            if answer == "helicopter":
                print(
                    "Bad choice, you don't know how to fly a helicopter, you crash into the hill and blow up. Game over")
            else:
                print(
                    "You drive away and find a safe place to rest. Congratulations, you have won the game")

    elif answer == "right":
        print("You chose a dangerous path, you fall off a cliff and die. Game over")

    else:
        print("Invalid choice, game over")

else:
    print("That's too bad, come back when you're ready to play")
