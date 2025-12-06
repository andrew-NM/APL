import re

text = "I know Python, Java, and C++  but not Ruby."

extracted_languages = re.findall(r"(python|java|c\+\+|ruby)", text, re.IGNORECASE)

print(extracted_languages)