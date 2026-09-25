import time

state = "green"

while True:
    if state == "green":
        print("GREEN LIGHT")
        time.sleep(5)
        state = "yellow"
    elif state == "yellow":
        print("YELLOW LIGHT")
        time.sleep(1)
        state = "red"
    elif state == "red":
        time.sleep(5)
        print("RED LIGHT")
        state = "green"