password_flag = False

def assess_strength():
    if password.upper() == password:
        print("WEAK")
    elif password.lower() == password:
        print("WEAK")
    elif int(password) == password:
        print("WEAK")

def assess_strength2():
    for char in password:
        if type(password(0)) == type(char):
            print("loop")

while password_flag == False:
    password = input("Enter password: ")
    if len(password) < 6:
        print("Password invalid.  Your password should be at least 6 characters.")
    elif len(password) > 12:
        print("Password invalid.  Your password should be no more than 12 characters.")
    else:
        print("Password accepted.")
        password_flag = True

assess_strength2()
