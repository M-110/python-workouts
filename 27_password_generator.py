"""
In this exercise, we’re going to create a password-generation function. 
Actually, we’re going to create a factory for password-generation functions. 
That is, I might need to generate a large number of passwords, all of which 
use the same set of characters. You’ll thus call the function create_password 
_generator with a string. That string will return a function, which itself
 takes an integer argument. Calling this function will return a password of 
 the specified length, using the string from which it was created; for example
"""

import random

def password_factory(s):
    def pass_gen(length):
        return ''.join(random.choices(s, k=length))
    return pass_gen

a_pass = password_factory('abcdef')
s_pass = password_factory('!@#$%^&*')

print(a_pass(10))
print(a_pass(5))
print(s_pass(10))
print(s_pass(20))