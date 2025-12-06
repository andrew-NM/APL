import re

text = "I love #Python and #AI"

pattern = re.findall('#[A-z]+', text)

print(pattern)