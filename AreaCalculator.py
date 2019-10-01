#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      prajakta
#
# Created:     17-09-2019
# Copyright:   (c) prajakta 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
""" This calculates area of few different shape """


pi=3.14159

def get_circle_area(radius):
    """a help similar to the abs function"""
    return pi*(radius**2)

def get_square_area(side):
    return side**2



def get_rectangle_area(width,height):
    return width*height