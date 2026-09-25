state = "living room"

while True:
    if state == "living room":
        print("You are in the living room")
        print("Your Options: feeling hungry?, feeling tired?, feeling bored?, feeling happy?, quit")
        feeling = input("How are you feeling?").strip().lower()

        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()

        if feeling == "hungry":
            state = "hungry"
        elif feeling == "tired":
            state = "tired"
        elif feeling == "bored":
            state = "bored"
        elif feeling == "happy":
            state = "happy"

# hungry state - in kitchen
    if state == "hungry":
        print("You are in the kitchen")
        print("Options: cook food, stare into fridge, stay hungry, go to living room, quit")
        feeling = input("What do you want to do?").strip().lower()

    if feeling in ["quit", "exit"]:
        print("Goodbye!")
        exit()

    if feeling == "cook food":
        state = "cook food"
    elif feeling == "stare into fridge":
        state = "stare into fridge"
    elif feeling == "stay hungry":
        state = "stay hungry"
    elif feeling == "go to living room": #back to start
        state = "living room"

    if state == "cook food":
        print("You are full and good to go!")
        print("Type quit to end game")
        feeling = input("Yay").strip().lower()



        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()

    elif state == "stare into fridge":
        print("You closed the refridgerator door and walked away")
        print("Type quit to end game")
        feeling = input("welp").strip().lower()

        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()

    elif state == "stay hungry":
        print("You starved, so well oh well")
        print("Type quit to end game")
        feeling = input("").strip().lower()

        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()

    # tired - in room and sleeping
    elif state == "tired":
        print("You are in your bedroom feeling exhausted.")
        print("Options: wake up, look at phone, quit")
        print("Type quit to end game")
        feeling = input("What do you want to do?").strip().lower()

        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()

        if feeling == "wake up":
            state = "living room"  # back to living room
        elif feeling == "look at phone":
            state = "bored"

    # bored
    elif state == "bored":
        print("Play games, Listen to music, Go for walk, Go to living room")
        print("Type quit to end game")
        feeling = input("What do you want to do?").strip().lower()

    if feeling == "play games":
        state = "Play games"
    elif feeling == "listen to music":
        state = "Listen to music"
    elif feeling == "go for walk":
        state = "Go for walk"
    elif feeling == "go to living room": #back to start
        state = "living room"

    if state == "Play games":
        print("You are playing Blockblast")
        print("You have a high-score of 3,826,709")
        print("Type quit to end game")
        feeling = input("").strip().lower()

    if feeling in ["quit", "exit"]:
        print("Goodbye!")
        exit()

    elif state == "Listen to music":
        print("You are listening to Kid Cudi")
        print("Type quit to end game")
        feeling = input("").strip().lower()

    if feeling in ["quit", "exit"]:
        print("Goodbye!")
        exit()

    elif state == "Go for walk":
        print("Cool breeze hits you, dogs barking, kids laughing")
        print("You felt at peace")
        print("Type quit to end game")
        feeling = input("").strip().lower()

    if feeling in ["quit", "exit"]:
        print("Goodbye!")
        exit()

    elif state == "happy":
        print("You are filled with joy and positive energy!")
        print("Options: do a dance, call a friend, go to living room, quit")
        feeling = input("What do you want to do? ").strip().lower()

        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()

        if feeling == "do a dance":
            state = "do a dance"
        elif feeling == "call a friend":
            state = "call a friend"
        elif feeling == "go to living room":
            state = "living room"

    elif state == "do a dance":
        print("Dalexa is playing and you lowkey start hitting them moves.")
        print("Type quit to end game")
        feeling = input("Woohoo!").strip().lower()

        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()

    elif state == "call a friend":
        print("You and your friend chat all night long!")
        print("Type quit to end game")
        feeling = input("hashtag fire!").strip().lower()

        if feeling in ["quit", "exit"]:
            print("Goodbye!")
            exit()
