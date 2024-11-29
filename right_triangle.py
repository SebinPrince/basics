'''AUTHOR:SEBIN PRINCE
DESCRIPTION:A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.
'''
def triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        print("Right triangle")
    else:
        print("Not a right triangle")
side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))
triangle(side1, side2, side3)
