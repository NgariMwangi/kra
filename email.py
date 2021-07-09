email=str(input("Enter Email"))

if email[0:]=="@" or email[0:]==".":
    print("email valid")
else:
    print("email is invalid")
