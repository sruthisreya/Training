import re
def is_valid_email(email):
    
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex,email)
valid_emails=[
    "example.email@gmail.com",
    "user_name123@yahoo.com",
    "john-doe@domain.org"
]

invalid_emails=[
    "@missingusername.com",
     "plainaddress",
    "username@.com"
]
for email in valid_emails:
    print(f"{email}  :True")

for email in invalid_emails:
    print(f"{email}   :False")

