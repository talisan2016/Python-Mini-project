def CheckEmail(email):
    email=email.strip()
    if len(email)==0:
        print("Email cann't be empty")
    elif not('.' in email and '@' in email):
        print("email must \".\" and \"@\"")
    elif email.count('@')!=1:
       print("email must contain only one @")
    elif not(email.endswith(('.com','.org','.net'))):
        print("email must end with .com/.org/.net")
    elif len(email)>=256:
        print("email not be more then 256")
    elif not(email[0].isalpha() and email[-1].isalpha()):
        print("Email cann't contain other values without 0-9A-Za-z_")
    else:
        print("valid email")

def main():
    email=input("Email : ")
    CheckEmail(email)

main()