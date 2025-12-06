import re

text = "This is is a test test"
matches = re.findall(r'\b(\w+)\s\1\b', text)
expected_matches = [f"{word} {word}" for word in matches]

print(expected_matches)