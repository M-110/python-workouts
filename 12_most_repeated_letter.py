"""
Write a function, most_repeating_word, that takes a sequence of strings as 
input. The function should return the string that contains the greatest number 
of repeated letters. In other words

- For each word, find the letter that appears the most times.

- Find the word whose most-repeated letter appears more than any other.
"""

def most_repeating_word(words):
    return sorted(words, 
                  key=lambda word: max(word.count(letter) for letter in word),
                  reverse=True)[0]

words = ['this', 'is', 'an', 'elementary', 'test', 'example']

assert(most_repeating_word(words) == 'elementary')