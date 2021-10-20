kenai2 = ["Rhoda", "Mark", "George", "Irene"]

username = input("Input your name: ")
while username not in kenai2:
    print("Try again!")
    username = input("Input your name: ")
else:
    print("Authenticated")