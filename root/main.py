state = "coding"


while True:
   if state == "coding":
       print("You are coding!")
       while True:
           feeling = input("How are you feeling? ").strip().lower()


           if feeling in ["quit", "exit"]:
               print("Goodbye!")
               exit()


           if feeling in ["tired", "hungry", "happy"]:
               if feeling == "tired":
                   state = "sleeping"
               elif feeling == "hungry":
                   state = "eating"
               else:
                   state = "coding"
               break
           else:
               print("Invalid input. Please enter 'tired', 'hungry', or 'happy'.")


   elif state == "eating":
       print("You are eating!")
       while True:
           feeling = input("How are you feeling? ").strip().lower()


           if feeling in ["quit", "exit"]:
               print("Goodbye!")
               exit()


           if feeling in ["hungry", "full", "tired"]:
               if feeling == "hungry":
                   state = "eating"
               elif feeling == "full":
                   state = "coding"
               else:
                   state = "sleeping"
               break
           else:
               print("Invalid input. Please enter 'hungry', 'full', or 'tired'.")


   elif state == "sleeping":
       print("You are sleeping!")
       while True:
           feeling = input("How are you feeling? ").strip().lower()


           if feeling in ["quit", "exit"]:
               print("Goodbye!")
               exit()


           if feeling in ["hungry", "awake", "tired"]:
               if feeling == "hungry":
                   state = "eating"
               elif feeling == "awake":
                   state = "coding"
               else:
                   state = "sleeping"
               break
           else:
               print("Invalid input. Please enter 'hungry', 'awake', or 'tired'.")

