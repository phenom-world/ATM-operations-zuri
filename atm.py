from datetime import datetime
import random

# create a database for existing users
database = {
    'Ubay': ['1234', 3000],
    'Sola': ['8567', 2000],
    'Adewumi': ['3432', 302]
}


def bank():
    print(datetime.now())
    print("Welcome to Tyler's bank ATM")
    haveAccount = input("Do you have an account with us? (1) Yes (2) No \n")
    if haveAccount == "1":
        login()
    elif haveAccount == "2":
        print("You do not have account with us")
        Register = int(
            input("Will you like to open an account with us? (1) Yes (2) No \n"))
        if Register == 1:
            register()
        else:
            print("Alright, Thanks and Take Care.")
    else:
        print("You have entered an invalid option; input \"1\" or \"2\"")
        bank()

# Generate account number


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

# Create Password


def passwordCreate():
    passw = input("Create a password \n")
    if len(passw) > 10:
        print("Your password is longer than 10 digits ")
        passwordCreate()
    return passw

# Register account


def register():
    print("===================")
    print("Register")
    Name = input("Enter your firstname \n")
    password = passwordCreate()
    accountNumber = generateAccountNumber()

    database[Name] = [password, 0]
    print("Your account has been successfully created")
    print("============================")
    print("This is your account number: ", accountNumber)
    print("= ==== ==== == ===== ===== =====")

    options = int(
        input("Will you like to login to your account? (1) Yes (2) No \n"))
    if options == 1:
        login()
    else:
        print("Thanks for Banking With Us")


# login


def login():
    print("************Login************* ")
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database and password == database[name][0]):
        print("Welcome " + name)
        operations(name)
    else:
        print("Invalid Username or Password. Please try again")
        login()

# ATM operations


def operations(name):
    print("You have successfully logged in")
    print('These are the available options')
    print('1. Withdrawal')
    print('2. Cash deposit')
    print('3. Complaints')
    print('4. Logout')
    selectedOption = input('Please select an option \n')
    if selectedOption == "1":
        Withdrawal(name)
    elif selectedOption == "2":
        cashDeposit(name)
    elif selectedOption == "3":
        complaint()
    elif selectedOption == "4":
        login()
    elif selectedOption == "5":
        print("Thanks for Choosing Tyler's Bank")
        exit()
    else:
        print('Invalid option selected, please try again')
        operations(name)

# Cash Deposit


def cashDeposit(name):
    if name:
        amount_to_deposit = int(input("Enter amount to deposit "))
        database[name][1] += amount_to_deposit
        print("Money recieved")
        print("Your new balance is:", database[name][1])
        operations(name)

# Cash Withdrawal


def Withdrawal(name):
    print("You have selected option 1")
    amount_to_withdraw = int(input("Enter amount you want to withdraw \n"))
    if database[name][1] > amount_to_withdraw:
        database[name][1] -= amount_to_withdraw
        print("Take your cash")
        print("New balance: ", database[name][1])
    else:
        print("You have insufficient balance")
        operations(name)

# Complaint


def complaint():
    complain = input("Enter your complain\n")
    print("Your complain is duly noted")
    bank()


bank()
