import re

phone_number = input("Please enter a phone number: ")
pattern = r'^\+?\d{1,3}-\d{3}-\d{4}$'

if re.match(pattern, phone_number):
    print(f"{phone_number} => Valid")
else:
    print(f"{phone_number} => Invalid")