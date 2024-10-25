'''AUTHOR:SEBIN PRINCE
DATE:25/10/24
DESCRIPTION:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c5=f−329

    For Celsius to Fahrenheit conversion:
    f=(95×c)+32

    For Fahrenheit to Celsius conversion:
    c=59×(f−32)

Sample Input 1:

Enter temperature: 100
Is this in (C)elsius or (F)ahrenheit? C

Sample Output 1:

100 Celsius is 212.0 Fahrenheit.

Sample Input 2:

Enter temperature: 32
Is this in (C)elsius or (F)ahrenheit? F

Sample Output 2:

32 Fahrenheit is 0.0 Celsius.

temp_1=int(input("enter temperature:"))
scale=str(input("Is this in (C)elsius or (F)ahrenheit?"))
if scale=="c":
    f=(9/5*temp_1)+32
    print(temp_1,"celcius to",f)
else:
    g=5/9*(temp_1-32)
    print(temp_1,"farenheit to",g)
'''

