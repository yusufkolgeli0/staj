import re

password=input("enter your password: ")


if len(password)<8:
    print("password must contain at least 8 characters")
elif not re.search("[A-Z]",password):
    print("password must contain at least 1 uppercase letter")
elif not re.search("[a-z]",password):
    print("password must contain at least 1 lowercase letter")
elif not re.search("[0-9]",password):
    print("password must contain at least 1 digit")
else:
    print("password is strong")