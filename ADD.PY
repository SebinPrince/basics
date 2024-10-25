'''AUTHOR:SEBIN PRINCE
DATE:25/10/24
DESCRIPTION:Sum of the numbers?
number=int(input("enter number:"))
sum_of_digits=0
while number>0:
    remainder=number%10
    sum_of_digits=sum_of_digits+remainder
    number=number//10
print("sum is:",sum_of_digits)
'''

