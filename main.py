while True:
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
            answer = input(
                "You go right and come across a little lake, would you like to swim across it or take a boat?")

            if answer == "swim":
                print(
                    "You start swimming and almost make it when a big fish comes to the surface and eats you. Game over")

            else:
                print("Good choice, you make it across the lake and find a cherry tree")

                answer = input(
                    "Would you like to eat some cherries?")

                if answer == "yes":
                    print(
                        "Oh no! The cherries have poisoned you. You die instantly. Game over")
                else:
                    print(
                        "Good choice, you have reached the escape point and have won the game")

        else:
            print("Invalid choice, game over")

    else:
        print("That's too bad, come back when you're ready to play")
        break
