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
import Converter
reload (Converter)

"""Test for Ex1: Converting 10 miles to kms. """
def main():
    pass

if __name__ == '__main__':
    main()

mi = 10
kms = Converter.miles_to_km(mi)

"""Test for Ex3: Converting 10,000 sqaure metres to hectares."""
print (str(mi) + " miles = "  + "{:.2f} kms.".format(kms))
print("The distance is " + "{:.2f} kms.".format(kms))

sqm = 10000
hec = Converter.sqmetres_to_hectares(sqm)
print(str(sqm) + " square metres = " + str(hec) + " hectare.")

"""Test for Ex5: Converting acres to edge of a square:"""
acre = 2
sqfeet = Converter.acres_to_eqge_of_square(acre)
print(str(acre) + " acres = " + str(sqfeet) + " square feet.")

sec = 05
min = 25 + (sec / 60)
degree = 95 + (min / 60)
deg = Converter.dms_to_dd(sec)
#print(str(degree) + ":" + str(min) + ":0" + str(sec) + "= {:.4f}".format(deg, min, sec) + ".")
print('{}:{}:0{} = {:.4f}'.format(degree, min, sec, deg))

kms_fuel = 100
km_per_lit = 8
dollar_per_lit = 1.50
fuel_cost = Converter.get_fuel_cost(kms_fuel)
print(str(kms_fuel) + " kms at " + str(km_per_lit) + " kms / litre and ${:.2f}".format(dollar_per_lit) +
" per year will cost ${:.2f}".format(fuel_cost))