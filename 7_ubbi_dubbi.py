"""
For this exercise, you’ll write a function (called ubbi_dubbi) that takes a 
single word (string) as an argument. It returns a string, the word’s 
translation into Ubbi Dubbi. So if the function is called with octopus, the 
function will return the string uboctubopubus. And if the user passes the 
argument elephant, you’ll output ubelubephubant.
"""

def ubbi_dubbi(word):
    return ''.join(char if char not in 'aeiou' else 'ub' + char for char in word)

assert(ubbi_dubbi('octopus') == 'uboctubopubus' and 
       ubbi_dubbi('elephant') == 'ubelubephubant')