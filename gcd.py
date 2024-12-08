'''AUTHOR:SEBIN PRINCE
DESCRIPTION:Recursive function to find the greatest common divisor of two positive numbers.
'''
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
a = int(input("Enter the first positive number: "))
b = int(input("Enter the second positive number: "))
result = GCD(a, b)
print("The Greatest Common Divisor (GCD) is:", result)
