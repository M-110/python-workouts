"""
In this exercise, write a function, passwd_to_dict, that reads from a 
Unix-style “password file,” commonly stored as /etc/passwd, and returns a dict 
based on it. If you don’t have access to such a file, you can download one 
that I’ve uploaded at http://mng.bz/2XXg.
"""
def create_dict(file_name):
    output_dict = {}
    with open(file_name) as file:
        for line in file:
            if line.startswith('#'):
                continue
            split_line = line.split(':')
            output_dict[split_line[0]] = split_line[2]
    return output_dict

database = create_dict('passwords.txt')

for user in database.items():
    print(user)