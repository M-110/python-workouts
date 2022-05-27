# -*- coding: utf-8 -*-
"""
In this exercise, write a function (get_final_line) that takes a filename as 
an argument. The function should return that file’s final line on the screen.
"""

def get_final_line(file_name):
    last_line="Error occured. No lines found in file."
    with open(file_name) as file:
        for line in file:
            last_line = line
    return last_line

print(get_final_line('test_file.txt'))