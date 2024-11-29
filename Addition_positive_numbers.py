'''AUTHOR:SEBIN PRINCE
DESCRIPTION:Recursive function to add two positive numbers.
'''
def add(num_1,num_2):
    if num_1==0:
        return num_2
    elif num_2==0:
        return num_1
    else:
        return add(num_1+1,num_2-1)
num_1=int(input("Enter first number:"))
num_2=int(input("Enter second number:"))
result=add(num_1,num_2)
print("Addition of two numbers is:",result)
