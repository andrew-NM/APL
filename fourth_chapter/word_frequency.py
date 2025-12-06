import re

text = "Python, Python! AI is great; Python AI."
word_frequency = dict()

clean_text = re.sub(r'\W', ' ', text).split()

for word in clean_text:
    word_frequency[f"{word}"] = clean_text.count(word)

print(word_frequency)