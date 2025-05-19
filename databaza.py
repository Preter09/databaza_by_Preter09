import json

databaza = {}


def save_databaza():
    with open("databaza.json", "w") as f:
        json.dump(databaza, f)

def load_databaza():
    global databaza
    try:
        with open("databaza.json", "r") as f:
            databaza = json.load(f)
    except FileNotFoundError:
        pass

# Call this at the start of your script
load_databaza()
# After successful registration, call save_databaza()
def register():
    print("Welcome!")
    registerName = input("Enter your name: ")
    registerPassword = input("Enter your password: ")
    if registerName in databaza:
        print("Name already exists.")
        return False
    else:
        databaza[registerName] = registerPassword
        save_databaza()
        print("Registration successful!")
        return True
    
def login():
    print("Welcome back!")
    loginName = input("Enter your name: ")
    loginPassword = input("Enter your password: ")
    if loginName in databaza and databaza[loginName] == loginPassword:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials.")
        return False

load_databaza

ask = input("Do you want to register or login? (r/l): ")


if  ask == "r" or ask == "R":
    register()
elif ask == "l" or ask == "L":
    login()
else:
    print("Error")
    exit()
