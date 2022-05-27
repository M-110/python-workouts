"""
In this exercise, I want you to write a function that takes a filename as an 
argument. It returns a string with the file’s contents, but with each word 
translated into Pig Latin, as per our plword function in chapter 2 on 
“strings.” The returned translation can ignore newlines and isn’t required to 
handle capitalization and punctuation in any specific way.
"""

file_path = 'file_20.txt'

def pig_latin_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return (' '.join(
            word + 'way' if word[0] in 'aeiou' else word[1:] + word[0] + 'ay'
            for word in f.read().replace('\n',' ').split()))
    
print(pig_latin_file(file_path))