def addAccount():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open("accounts.txt", "a") as accountFile:
        accountFile.write("Username: " + username + " | Password: " + password + "\n")

def viewAccounts():
    pass

while True:
    choice = input("Would you like to (a)dd to the list or (v)iew the list? Press q to quit... " + "\n")

    if choice == "q":
        break

    if choice == "a":
        addAccount()
    elif choice == "v":
        viewAccounts()
    else:
        print("Invalid choice.")