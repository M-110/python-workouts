"""
For this exercise, write a Python function (pig_latin) that takes a string as 
input, assumed to be an English word. The function should return the 
translation of this word into Pig Latin. You may assume that the word contains 
no capital letters or punctuation.
"""

def pig_latin():
    input_string = input("Translate from English to Pig Latin: ")
    if input_string[0] in 'aeiou':
        print(input_string + 'way')
    else:
        print(input_string[1:] + input_string[0] + 'ay')

    