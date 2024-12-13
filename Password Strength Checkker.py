#password stregth checker

import re   #regular expression module
password = input("Enter a Password =")
suggestion = []
  
if len(password) >= 8:  #checking length of password
    if re.search(r'[A-Z]',password):    #checking for capital letter
        if re.search(r'[a-z]',password):    #checking for small letters
            if re.search(r'\d',password):   #checking for digits
                if re.search(r'[!@#$%^&*()-=_+<>/?:""'']',password):    #checking for special characters
                    print("Password is Strong") #if all satisfied 
                else:
                    suggestion.append("Password Should Contain Special Characters")
            else:
                suggestion.append("Password Should Contain Digits")
        else:
            suggestion.append("Password Should Contain small Characters")
    else:
        suggestion.append("Password Should Contain capital Characters")
else:
    suggestion.append("Password Should Contain 8 or more than 8 Characters")

