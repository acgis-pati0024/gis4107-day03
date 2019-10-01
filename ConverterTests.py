

import Converter
reload (Converter)

<<<<<<< HEAD
"""Test for Ex1: Converting 10 miles to kms. """
def main():
    pass

if __name__ == '__main__':
    main()

mi = 10
kms = Converter.miles_to_km(mi)

print (str(mi) + " miles = "  + "{:.2f} kms.".format(kms))
print("The distance is " + "{:.2f} kms.".format(kms))

"""Test for Ex2: distance in kph to m/s:"""
kph = 10000
mps = Converter.kmperHour_to_mPerSec(kph)

print (str(kph) + " km per hour is equal to " + "{:.4f} metres per second.".format(mps))

"""Test for Ex3: Converting 10,000 sqaure metres to hectares."""
sqm = 10000
hec = Converter.sqmetres_to_hectares(sqm)
print(str(sqm) + " square metres = " + str(hec) + " hectare.")

"""Test for Ex5: Converting acres to edge of a square:"""
acre = 2
sqfeet = Converter.acres_to_eqge_of_square(acre)
print(str(acre) + " acres = " + str(sqfeet) + " square feet.")

"""Test for Ex6: population of bears per square km:"""
bear_count = 4
density = Converter.get_bear_count(bear_count)
print ("The population density of " + str (bear_count) + " bears is {:.2f} ".format(density) + "bears per sqare km.")


sec = 05
min = 25 + (sec / 60)
degree = 95 + (min / 60)
deg = Converter.dms_to_dd(sec)
#print(str(degree) + ":" + str(min) + ":0" + str(sec) + "= {:.4f}".format(deg, min, sec) + ".")
print('{}:{}:0{} = {:.4f}'.format(degree, min, sec, deg))


"""test for Ex9: Converting kilometres to dollars per litre:"""
kms_fuel = 100
km_per_lit = 8
dollar_per_lit = 1.50
fuel_cost = Converter.get_fuel_cost(kms_fuel)
print(str(kms_fuel) + " kms at " + str(km_per_lit) + " kms / litre and ${:.2f}".format(dollar_per_lit) +
" per year will cost ${:.2f}".format(fuel_cost))
=======
#inches = 18
#ft = Converter.inches_to_feet(inches)
#print "{} inches = {:.2f} feet".format(inches, ft)

miles=input("Enter Miles:")

Km= Converter.miles_to_km(miles)

print str(miles) + " miles = " + str(Km)+" Km."

#---------------------------------

#function call convert.sqmetres_to_hectares

sqmeter=float(input("Enter Square meter:"))
hectares=Converter.sqmetres_to_hectares(sqmeter)
print str(sqmeter) + " sqmtr = " + str(hectares)+" hectares."

#--------------------------
#function call convert.acres_to_edge_of_square


acre = float(input("Enter value in Acres:"))
sq_metr = Converter.acres_to_edge_of_square(acre)
print("The edge length of " + str(acre) + " acres squared is " + str(sq_metr) + " Sqaure metres.")

#---------------------------------


#function call get_bear_count(sqmtr)
densityPerKm = int (input("Enter Number of Bear per sqkm:"))

sqmtr=int(input("Enter area in sqmtr : "))

denPermtr= Converter.get_bear_count(sqmtr,densityPerKm)

print "When bear density is "+str(densityPerKm)+" bears / sq. km and area is " + str(sqmtr)+ " sq m, the probably number of bears is "+ str(denPermtr)




#-----------------------------------
#function call convert.dms_to_dd


second = 05
minute = 25
degree = 95
dd=(Converter.dms_to_dd(degree,minute,second))
#print("dd"+str(dd))

print(str(degree) + ":"+ str(minute) + ":0" + str(second) + "=" + str(dd))

#-----------------------------------------

#function call dd_to_dms(dd)

dd=input("Enter Decimal degree")

minutes,seconds=Converter.dd_to_dms(dd)

print str(dd) + " Decimal Degree = " + str (degree) + ":"+ str(minutes)+":"+str(seconds)+" Degree Minutes Seconds"






#------------------------------------------------------
#function call convert.get_fuel_cost


km = 100
mi_per_gal = 35
dollars_per_Litre = 1.50
drive_cost=Converter.get_fuel_cost(km,mi_per_gal,dollars_per_Litre)


print(str(km) + " km at " + str(mi_per_gal) + " mi/gal and $" + str(dollars_per_Litre) + " per liter will cost $" + str(drive_cost))

>>>>>>> c42fba870adf9fd7307536e566b308fc5a9ed69e
