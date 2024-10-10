'''
Combining operations
'''
from operations import summation, subtraction

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
