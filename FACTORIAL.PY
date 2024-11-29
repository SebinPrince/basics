'''AUTHOR:SEBIN PRINCE
DESCRIPTION:Program to find the factorial of a number using Recursion.
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n - 1)
a=int(input("enter a number:"))
f=factorial(a)
print(f)
