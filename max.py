'''AUTHOR:SEBIN PRINCE
DESCRIPTION:. Write a Python function to find the maximum of three numbers. 
'''
def max(x,y,z):
    if (x>y) and (x>z):
        return x
    elif (y>x) and (y>z):
        return y
    else:
        return z
a=int(input("enter a number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
print(max(a,b,c))
