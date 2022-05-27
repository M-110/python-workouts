"""
For this exercise, create a function, passwd_to_csv, that takes two filenames 
as arguments: the first is a passwd-style file to read from, and the second is 
the name of a file in which to write the output.

The new file’s contents are the username (index 0) and the user ID (index 2). 
Note that a record may contain a comment, in which case it will not have 
anything at index 2; you should take that into consideration when writing the 
file. The output file should use TAB characters to separate the elements.
"""
import os

file_name = 'passwords.txt'
out_name = 'users.csv'

def passwd_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as in_f:
        with open(output_file, 'w', encoding="utf-8") as out_f:
            for line in in_f:
                if len(line.split(':')) > 1:
                    out_f.write(f"{line.split(':')[0]}\t{line.split(':')[2]}\n")
                
passwd_to_csv(file_name, out_name)

