'''AUTHOR=SEBIN PRINCE
DESCRIPTION=Write a python program to find a number is prime or not?
'''
a=int(input("enter number:"))
is_prime=True
for i in range(2,a):
    if a%i==0:
        is_prime=False
        break
if is_prime:
    print("prime")
else:
    print("not prime")
