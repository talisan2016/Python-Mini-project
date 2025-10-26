def checkPassword(password, email):
    def haslower(password):
        for i in password:
            if i.islower():
                return True
        return False

    def hasupper(password):
        for i in password:
            if i.isupper():
                return True
        return False

    password = password.strip()

    if len(password) < 8:
        print("Password must be greater than or equal to 8 characters.")
    elif password == email:
        print("Password and email can't be the same.")
    elif ' ' in password:
        print("Password can't contain spaces.")
    elif not (password[0].isalpha() and password[-1].isalpha()):
        print("Password must start and end with an alphabet.")
    elif not (haslower(password) and hasupper(password)):
        print("Password must contain at least one uppercase and one lowercase letter.")
    else:
        print("Valid password")


def main():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    checkPassword(password, email)


main()
