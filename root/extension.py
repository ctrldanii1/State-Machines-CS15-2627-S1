state = "home"

while True:

    if state == "home":
        print("\nYou are at HOME.")
        print("1. Go to school")
        print("2. Go to the mall")
        choice = input("What do you want to do? ").lower()

        if choice == "1":
            state = "school"
        elif choice == "2":
            state = "mall"
        else:
            print("Invalid choice. Try again.")

    elif state == "school":
        print("\nYou are at SCHOOL.")
        print("1. Go to class")
        print("2. Go home")
        choice = input("What do you want to do? ").lower()

        if choice == "1":
            state = "class"
        elif choice == "2":
            state = "home"
        else:
            print("Invalid choice. Try again.")

    elif state == "class":
        print("\nYou are in CLASS.")
        print("1. Study")
        print("2. Go to the mall")
        choice = input("What do you want to do? ").lower()

        if choice == "1":
            state = "school"
        elif choice == "2":
            state = "mall"
        else:
            print("Invalid choice. Try again.")

    elif state == "mall":
        print("\nYou are at the MALL.")
        print("1. Go home")
        print("2. Go to school")
        choice = input("What do you want to do? ").lower()

        if choice == "1":
            state = "home"
        elif choice == "2":
            state = "school"
        else:
            print("Invalid choice. Try again.")