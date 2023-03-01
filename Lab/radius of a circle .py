"""
Ask the user to enter the radius of a circle in order to alert its calculated
area and circumference
"""
import math 
Pi=math.pi
#! I can use pow or ** operators to calculate the area  :( 
#! 👉 never forget to convert inputs from strings to numbers
# print (math.pow(Pi,5))
# print(Pi**5)

while True:
    radius =input('radius of a circle :' )
    circumference = Pi *float(2) *float(radius)
    area = Pi*float(radius)*float(radius)
    format="the radius of a circle is {} \n circumferences are {} \n area is {} \n"
    print(format.format(radius,circumference,area))
