kenai2 = ["Rhoda", "Mark", "George", "Irene"]

username = input("Input your name: ")
for name in (kenai2):
    if username in kenai2:
        print("Authenticated!")
        break
    else:
        print("Try again!")
        username = input("Input your name")

        