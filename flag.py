kenai2 = ["Rhoda", "Mark", "George", "Irene"]

authenticated = False

while authenticated == False:
    username = input("Input your name: ")
    if username in kenai2:
        print("Authenticated!")
        authenticated = True
    else:
        print("Try again!")   
