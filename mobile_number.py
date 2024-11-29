'''AUTHOR:SEBIN PRINCE
DESCRIPTION:Program to check whether the given number is a valid mobile number or not using functions.

Rules:

    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9
    '''
def mobile_number(number):
    if len(number)==10 and number[0] in ["7","8","9"]:
        return True
    return False
mobile=input("enter number:")
if mobile_number(mobile):
    print("valid")
else:
    print("not valid")
    
