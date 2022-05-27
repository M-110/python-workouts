"""
In this exercise, write two functions. find_longest_word takes a filename as 
an argument and returns the longest word found in the file. The second 
function, find_all_longest_words, takes a directory name and returns a dict 
in which the keys are filenames and the values are the longest words from each 
file.
"""

import re


files_dict = {'The Strange Case Of Dr. Jekyll And Mr.Hyde': 'books/43-0.txt',
         'A Christmas Carol': 'books/46-0.txt',
         'Frankenstein': 'books/84-0.txt',
         'Pride and Prejudice': 'books/1342-0.txt',
         'Moby Dick': 'books/2701-0.txt',
         'Begin to Knit': 'books/61105-0.txt',
         'Dracula': 'books/pg345.txt',
         'Little Women': 'books/pg514.txt',
         'The Works of Edgar Allan Poe': 'books/pg25525.txt',
         'The Memoirs, Correspondence, And Miscellanies': 'books/pg28860.txt'}


def find_longest_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return max(((len(word), word) 
                    for word in re.sub(r'\W|_', ' ', f.read()).split())
                    ,key=lambda x: x[0])
    
def find_all_longest_words(files_dict):
    return {book[0]: find_longest_word(book[1]) for book in files_dict.items()}
    
result = find_all_longest_words(files_dict)

for book, word in result.items():
    print(f'{book}: {word[1]} ({word[0]})')
    
    