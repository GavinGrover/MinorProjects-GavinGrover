import re

def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

email = input("Enter an email address to validate: ")
if validate_email(email):
    print("Email is valid.")
else:
    print("Invalid email address.")
