"""
Filename: Warm-Up_7_Circle_Calculator.py
Author: <Santamaria, Oliver>
Created: <12/04/2025>
Instructor: Holtslander
"""

def circle_calculator():
    """
    Calculates the area and circumference of a circle.
    Asks the user to enter the radius of the circle.
    Uses the formulas
    A = pi*r**2
    C = 2*pi*r
    :return: None
    """
    ### YOUR CODE GOES HERE ###

radius = input("Enter the radius of the circle:\n")
radius = float(radius)
print(f"The area of the circle is:\n {3.14*(radius*radius)}")
print(f"The circumference of the circle is:\n {2*3.14*radius}")

### YOU SHOULD NOT NEED TO CHANGE ANYTHING HERE ###
if __name__ == '__main__':
    circle_calculator()