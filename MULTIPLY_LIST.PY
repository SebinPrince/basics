'''AUTHOR:SEBIN PRINCE
DESCRIPTION: Write a Python function to multiply all the numbers in a list
'''
def multiply(numbers):
    a = 1
    for x in numbers:
        a *= x
    return a
numbers = [2, 3, 4]
print(multiply(numbers))
