import random

VOWELS= "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = "ccvc"
word_str = ""
for kind in word_format:
    if kind == "c":
        word_str += random.choice(CONSONANTS)
    else:
        word_str += random.choice(VOWELS)
print(word_str.upper())

str.isupper()