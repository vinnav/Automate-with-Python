import re

# Write a function that uses regular expressions to make sure the password
# string it is passed is strong. 
# A strong password is defined as one that is:
# - at least eight characters long,
# - contains both uppercase and lowercase characters,
# - has at least one digit. 


strongPassword = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})')

def checkPasswordStrength(pwd):
    if re.match(strongPassword, pwd):
        return True
    else:
        return False

pwd = input("Enter your password: ")

if checkPasswordStrength(pwd):
    print("Your password is strong")
else:
    print("Your password is weak, it needs to contain 8 characters, at least a lower case, upper case and a number")

# setting up github


    