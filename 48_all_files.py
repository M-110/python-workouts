"""
In this exercise, I’d like you to create just such an iterator, using a 
generator function. That is, this generator function will take a directory 
name as an argument. With each iteration, the generator should return a single 
string, representing one line from one file in that directory. Thus, if the 
directory contains five files, and each file contains 10 lines, the generator 
will return a total of 50 strings--each of the lines from file 0, then each of 
the lines from file 1, then each of the lines from file 2, until it gets 
through all of the lines from file 4.
"""

import os

directory = "C:\\Users\\mclea\\Dropbox\\Python\\50Workouts"

def all_lines(directory):
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(os.path.join(directory, file)) as text_file:
                for line in text_file:
                    yield line

a = all_lines(directory)
