'''AUTHOR:SEBIN PRINCE
DESCRIPTION:A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.
'''
def right_triangle():
    a=int(input("Enter hypotenuse side:"))
    b=int(input("enter second side:"))
    c=int(input("enter third side:"))

    if a*a==b*b+c*c:
        print("right triangle")
    else:
        print("not right triangle")
right_triangle()
