'''AUTHOR:SEBIN PRINCE
DATE:25/10/24
DESCRIPTION:The number is armstrong or not?

number=int(input("enter number:"))
sum=0
while number>0:
    number=number%10
    sum=sum+number^3
    number=number//10
if sum==number:
    print("armstrong")
else:
    print("not armstrong")
    '''



