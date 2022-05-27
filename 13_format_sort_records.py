"""
For this exercise, write a Python function, format_sort_records, that takes 
the PEOPLE list and returns a formatted string that looks like the following:

Biden      Joe         7.85
Putin      Vladimir    3.63
Xi         Jinping    10.60
"""

PEOPLE = [('Joe', 'Biden', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(people):
    return'\n'.join(f'{person[1].ljust(10)}{person[0].ljust(10)}\t{person[2]:.3}' for person in people)

print(format_sort_records(PEOPLE))