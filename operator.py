'''AUTHOR=SEBIN PRINCE
DESCRIPTION=Create a simple calculator that perform a basic operation chosen by the user

a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
options=["=","-","%","*"]
choice=input("your choice +,-,%,*\nchoose:")
print(choice)
if (choice=="+"):
    c=a+b
    print(a,"+",b,"=",c)
elif (choice=="-"):
    c=a-b
    print(a,"-",b,"=",c)
elif (choice=="*"):
    c=a*b
    print(a,"*",b,"=",c)
elif(choice=="%"):
    c=a%b
    print(a,"%",b,"=",c)
else:
    print("invalid statement")
'''
