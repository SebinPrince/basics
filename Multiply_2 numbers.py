'''AUTHOR:SEBIN PRINCE
DESCRIPTION:Recursive function to multiply two positive numbers
'''
def multiply(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+multiply(num1,num2-1)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(multiply(num1,num2))
