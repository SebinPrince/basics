'''AUTHOR:SEBIN PRINCE
DESCRIPTION:
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 
'''
def factorial():
    f=1
    a=int(input("Enter a number:"))
    for i in range(1,a+1):
        f=f*i
    print(f)
factorial()
