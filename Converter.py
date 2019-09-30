#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jmpp
#
# Created:     17-09-2019
# Copyright:   (c) jmpp 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


"""Converts miles to kilometres."""
def miles_to_km(mile):
    miles = 10
    kms = miles * 1.609
    return kms

"""converts square metres to hectares."""
def sqmetres_to_hectares(sqm):
    sqm = 10000
    hectare = sqm / 10000
    return hectare

"""converts acres to area of length of a square."""
def acres_to_eqge_of_square(sq):
    acres = 2
    sq_feet = acres * 43560
    return sq_feet

def dms_to_dd(sec):
    second = 05
    minute = 25 + (second / 60)
    degree = 95 + (minute / 60)
    return degree

"""returns the average fuel cost for driving distance."""
def get_fuel_cost(cost):
    km = 100
    km_per_lit = 8
    dollars_per_lit = 1.50
    fuel_cost = km_per_lit * dollars_per_lit
    return fuel_cost