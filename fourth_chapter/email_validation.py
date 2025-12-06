import re

emails = ["user@example.com", "bad-email", "test@domain.org"]
pattern = '^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.(com|org|edu)$'

for email in emails:
    if re.match(pattern, email):
        print(f"{email} => Valid")
    else:
        print(f"{email} => Invalid")
