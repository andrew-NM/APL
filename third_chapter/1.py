def remove_vowels(text):
    vowels = "aeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result
    
text = "bat"
print(remove_vowels(text))
