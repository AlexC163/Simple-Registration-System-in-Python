logged_in = False


def startingScreen():
    while True:
        choice = input("Do you want to log in or sign up?: ").lower()
        if choice == "log in":
            logIn()
            break
        elif choice == "sign up":
            signUp()
            break
        else:
            print("Please enter a valid input (log in) (sign up).")


def logIn():
    print("Time to log in!")
    username = input("Enter your username/email: ")
    passcode = input("Enter your passcode: ")

    with open("data.txt", "r") as f:
        all_data = f.read().split("\n")

    for line in all_data:
        info = line.split(";")
        if str(info[0]) == username:
            if str(info[1]) == passcode:
                loggedIn(username)
                return
    print("You did not enter a valid username/passcode.")


def signUp():
    print("Time to sign up!")
    username = input("Enter your username/email: ")
    passcode = input("Enter your passcode: ")
    rpt_passcode = input("Repeat your passcode: ")

    while True:
        if passcode.__eq__(rpt_passcode):
            with open("data.txt", "a") as file:
                file.write(username + ";" + passcode + "\n")
                logIn()
                break
        else:
            print("Your passcodes do not match. Please try again.")


def loggedIn(username):
    print("Hello, " + username + ", You are logged in!")


startingScreen()
