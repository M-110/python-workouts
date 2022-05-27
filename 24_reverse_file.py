"""
In many cases, we want to take a file in one format and save it to another 
format. In this function, we do a basic version of this idea. The function 
takes two arguments: the names of the input file (to be read from) and the 
output file (which will be created).
"""

def reverse_file(in_file, out_file):
    with open(in_file, 'r', encoding='utf') as f_in:
        with open(out_file, 'w', encoding='utf') as f_out:
            for line in f_in:
                f_out.write(line.replace('\n', '')[::-1] + '\n')
                
reverse_file('in.txt', 'out.txt')