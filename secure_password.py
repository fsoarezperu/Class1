#from consolePys import Console
#from consolePys import activeColor
#activeColor() # make sure to call this when using cmd/powershell/etc
#Console.error  ("Hello, World!")
#Console.fail   ("Hello, World!")
#Console.logc   ("Hello, World!")
#Console.log    ("Hello, World!")
#Console.info   ("Hello, World!")
#Console.header ("Hello, World!")
#Console.warn   ("Hello, World!")

email = input("Email address:")
password = input("Password:")

import re

def check_password(password):
    if len(password) < 8:
        return False
    elif not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not re.search("[_@$]", password):
        return False
    else:
        return True

if check_password(password):
    print("this is a secure password.")
else:
    print("Not secure. please enter at least 8 digit password including capital letters , numbers and at least one special character.")
