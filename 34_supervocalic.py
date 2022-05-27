# -*- coding: utf-8 -*-
"""
For the purposes of this exercise, I’ll loosen the definition, accepting any 
word that has all five vowels, in any order and any number of times. Your 
function should find all of the words that match this definition 
(i.e., contain a, e, i, o, and u) and return a set containing them.

Your function should take a single argument: the name of a text file 
containing one word per line, as in a Unix/Linux dict. If you don’t have such 
a “words” file, you can download one from here: http://mng.bz/D2Rw.
"""

file_name = 'words.txt'

def supervocalic_words(file_name):
    vowels = set('aeiou')
    with open(file_name, 'r', encoding='utf-8') as f:
        return {word.strip() for word in f if vowels < set(word.lower())}
    
print(supervocalic_words(file_name))