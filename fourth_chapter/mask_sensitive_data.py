import re

text = "Card: 1234-5678-9012-3456"

masked_text = re.sub(r"\d{4}-", "****-", text)

print(masked_text)