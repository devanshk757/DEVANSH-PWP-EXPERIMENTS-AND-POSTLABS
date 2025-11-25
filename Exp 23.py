import re

# def validate_pan(pan):
#     pattern = r'[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    
#     if re.match(pattern, pan):
#         return True
#     else:
#         return False

# # Test the function
# pan_number = input("Enter PAN card number: ")
# if validate_pan(pan_number):
#     print("Valid PAN card number.")
# else:
#     print("Invalid PAN card number.")


# def validate_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(pattern, email):
#         return True
#     return False
# # Test the function
# email_id = input("Enter email ID: ")
# if validate_email(email_id):
#     print("Valid email ID.")
# else:
#     print("Invalid email ID.")



#-------------------------------------------------------------------------POST-LAB-------------------------------------------------------------------------
def validate_pan(pan):
    pattern = r'[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.match(pattern, pan))

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

pan = input("Enter PAN card number: ")
email = input("Enter email ID: ")

if validate_pan(pan):
    print("Valid PAN card number.")
else:
    print("Invalid PAN card number.")

if validate_email(email):
    print("Valid email ID.")
else:
    print("Invalid email ID.")


# Test the functions
pan_number = input("Enter PAN card number: ")
email_id = input("Enter email ID: ")

if validate_pan(pan_number):
    print("Valid PAN card number.")
else:
    print("Invalid PAN card number.")

if validate_email(email_id):
    print("Valid email ID.")
else:
    print("Invalid email ID.")
