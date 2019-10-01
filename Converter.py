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

"""converts degrees minutes seconds to decimal degrees."""
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

"""returns a distance in kilometres per hour to metres per second."""
def kmperHour_to_mPerSec(kilo):
    kph=10000.0000
    convKm=kph * 1000 / 3600
    return convKm

"""returns population density using population of bears."""
def get_bear_count(bear):
    bears = 4
    sq_m = 10000000
    sq_km = 0.000001* sq_m
    den_Per_m= bears*sq_km
    return den_Per_m