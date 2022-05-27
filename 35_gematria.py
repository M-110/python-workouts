"""
In this exercise, you’ll write two functions:

gematria_for, which takes a single word (string) as an argument and returns 
the gematria score for that word

gematria_equal_words, which takes a single word and returns a list of those 
dict words whose gematria scores match the current word’s score.
"""

import string

def alpha_num_keys():
    return {key: value for value, key in enumerate(string.ascii_lowercase, 1)}

def gematria_for(word):
    return sum(alpha_num_keys()[char.strip().lower().replace('-','')] 
               for char in word if char.strip().lower().replace('-',''))

def gematria_equal_words(word):
    value = gematria_for(word)
    with open('words.txt', 'r', encoding='utf-8') as f:
        return [match.strip() for match in f 
                if gematria_for(match) == value]
    
print(gematria_equal_words('cat'))