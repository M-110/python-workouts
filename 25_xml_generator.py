"""
Write a function, myxml, that allows you to create simple XML output. The 
output from the function will always be a string. The function can be invoked 
in a number of ways.
"""

def myxml(tag, inside='', **kwargs):
    keys=''
    if kwargs:
        keys = ''.join([f' {key}="{value}"' for key,value in kwargs.items()])
    print(f"<{tag}{keys}>{inside}</{tag}>")
    
myxml('foo')
myxml('foo', 'bar')
myxml('foo', 'bar', a=1, b=2, c=3)
