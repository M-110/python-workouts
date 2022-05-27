"""
For this exercise, you need to write a function (hex_output) that takes a hex
number and returns the decimal equivalent. That is, if the user enters 50, 
you’ll assume that it’s a hex number (equal to 0x50) and will print the value 
80 to the screen. And no, you shouldn’t convert the number all at once using 
the int function, although it’s permissible to use int one digit at a time.
"""

hex_keys = list('0123456789abcdef')

def hex_output(hex_number: str):
    return sum(hex_keys.index(symbol.lower()) * (16 ** i)
               for i, symbol in enumerate(hex_number[::-1]))

assert(int(0x4b5) == hex_output('4b5') and 
       int(0x6ff3f4520fab) == hex_output('6ff3f4520fab'))
