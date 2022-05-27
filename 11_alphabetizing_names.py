"""
Write a function, alphabetize_names, that assumes the existence of a PEOPLE 
constant defined as shown in the code. The function should return the list of 
dicts, but sorted by last name and then by first name.
"""

PEOPLE = [
     {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'},
    {'first':'Reuven', 'last':'Adam',
    'email':'reuven@lerner.co.il'},
     {'first':'John', 'last':'Johnson',
    'email':'johnsonjohn@johnson.edu'},
     {'first':'Adam', 'last':'Johnson',
    'email':'johnsonadam@johnson.edu'},
 ]

def alphabetize_names(people):
    return sorted(people, key=lambda person: (person['last'], person['first']))
                  
ordered_people = alphabetize_names(PEOPLE)

for person in ordered_people:
    print(person)
    