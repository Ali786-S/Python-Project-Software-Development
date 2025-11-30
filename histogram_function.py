# I declare that my work contains no examples of misconduct, such as plagarism, or collusion.
# Any code taken from other sources is referenced within my code solution
# Student ID: w20457325
# Date: 23/11/2023
from graphics import *
#Import graphics module to use the elements

#Define a function for creating the histogram bars
def histogram_bars(win, x, height, color, label):
    bar = Rectangle(Point(x, 400), Point(x + 70, 400 - height * 5)) #Creates a rectangle representing the bars
    bar.setFill(color) #set a fill colour for the rectangle 
    bar.draw(win) #Draw the rectangle on the graphics window

    