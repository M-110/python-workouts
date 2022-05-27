"""
The challenge for this exercise is to write a wordcount function that 
mimics the wc Unix command. The function will take a filename as input and 
will print four lines of output:

Number of characters (including whitespace)

Number of words (separated by whitespace)

Number of lines

Number of unique words (case sensitive, so “NO” is different from “no”)
"""


def wordcount(file_name):
    with open(file_name) as file:
        line_count = 0
        char_count = 0
        word_count = 0
        word_set = set()
        for line in file:
            line_count += 1
            char_count += len(line)
            word_count += len(line.split())
            word_set.update(line.split())
        unique_count = len(word_set)
        
        print(f'Word count: {word_count}')
        print(f'Character count: {char_count}')
        print(f'Unique word count: {unique_count}')
        print(f'Line count: {line_count}')
        
wordcount('file_20.txt')
            
