'''
Combining operations
'''
from operations import summation, subtraction


# This is some code that doesn't work, and therefore
# it is commented out. We should remove it at
# some point:

# def perform_operation(num1, num2, operation):
#     if operation = "add":
#         result = summation(num1, num2)

#     return result

#num1 - indicate the first number
#num2 - indicate the second number
#operation - select the operation 'add' or 'subtract'
#results - result of the operation selected

def perform_operation(num1, num2, operation):
    if operation == "add":
        result = summation(num1, num2)
    elif operation == "subtract":
        result = subtraction(num1, num2)
    else:
        raise ValueError("Invalid operation. Please choose 'add' or 'subtract'.")

    return result
