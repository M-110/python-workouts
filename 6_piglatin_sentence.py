"""
translate a series of English words into Pig Latin. Write a function called 
pl_sentence that takes a string containing several words, separated by spaces. 
(To make things easier, we won’t actually ask for a real sentence. More 
 specifically, there will be no capital letters or punctuation.)
"""

def pl_sentence():
    input_string = input("Translate sentence to Pig Latin: ")
    output = []
    
    for word in input_string.split():
        if word[0] in 'aeiou':
            output.append(word + 'way')
        else:
            output.append(word[1:] + word[0] + 'ay')
    print(' '.join(output))
    

# One line version

def pl_sentence2():
    print(' '.join(
            word + 'way' if word[0] in 'aeiou' else word[1:] + word[0] + 'ay'
            for word in input("Translate sentence to Pig Latin: ").split()))
