'''AUTHOR:SEBIN PRINCE
DATE:19/10/24
Write a Python program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between and store the result in a new variable.

    Print the concatenated string.

    From the concatenated string:
    Access and print a sub-string that consists of the first name only. Use string slicing to extract the sub-string.
first_name=input("enter your first name:")
last_name=input("enter your second name:")
name=first_name+" "+ last_name
print("name is",name)
first_namelength=len(first_name)
print(first_namelength)
extractedfirst_name=name[:first_namelength]
print(extractedfirst_name)
'''







