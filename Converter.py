#-------------------------------------------------------------------------------
# Name:        Converter.py
# Purpose:     Various unit conversions for GIS4107 - Exercises for Week 3
# Author:      David Viljoen
# Created:     02/10/2015
#-------------------------------------------------------------------------------

# Exercise 1
#def inches_to_feet(inches):
  #  """inches_to_feet(inches) -> ft

 #   Converts length from inches to feet"""

  #  feet_per_inch = 1 / 12.0
  #  feet = inches * feet_per_inch
   # return feet

#---------------------------------------------------------------
#Exercise 1 Miles to kilometer

def miles_to_km(miles):
    """ miles_to_km converts miles to km and returns value in km"""

    km = miles * 1.609

    return km
#----------------------------------------------------------------
#Exercise 3

def sqmetres_to_hectares( sqmtr):
    """ This function converts square mteres to hectares"""

    hectares=float(sqmtr/10000)
    return hectares

#----------------------------------------------------------------------
#Exercise 5

def acres_to_edge_of_square(acres):
    """This function converts acres to sqaure meter """
   # sqft=acres*43560
    sqmtr=acres*4046.86
    return sqmtr
#----------------------------------------------------------------------
#Exersice 6


def get_bear_count(sqmtr,densityPerKm):
    sqKm =int(0.000001*sqmtr)
    denPermtr= int(densityPerKm*sqKm)
    #print(denPermtr)
    return denPermtr




#----------------------------------------------------------------------
#Exercise 7

def dms_to_dd(degree,minute,second):
    """THis function converts decimal minutes seconds to decimal degree"""

    seconds = second/3600.0
    minutes = minute/60.0 #+ (second/60)
    #degrees = degree #+ (minute/60)
    #print "minute"+str(minute)
   # degree= minute / 60
    dd = degree + (minutes) +( seconds)

    return (dd)

#----------------------------------------
#exersise 8

def dd_to_dms(dd):
    dd1=abs(float(dd))
    degree=int(dd1)
    mins=dd1-degree
    minConv=mins*60
    minutes= int(minConv)
    secIndd=minConv-minutes
    seconds=int(secIndd*60)
    return minutes,seconds

#----------------------------------------
#exersise 9
def get_fuel_cost(km,mi_per_gal,dollars_per_Litre):
    km_per_litre=(mi_per_gal*1.609)/3.785
   # km_per_litre = 8
   # print (str(km_per_litre))
    drive_cost = (km/km_per_litre) * dollars_per_Litre
    return drive_cost

































