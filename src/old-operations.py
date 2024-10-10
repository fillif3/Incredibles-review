'''
This is an older version of the code in operations.py
and it could be deleted but we haven't done it because
we were not using version control a year ago.
'''

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")

def mult(a, b):
    return a * b 