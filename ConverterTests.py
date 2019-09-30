

import Converter
reload (Converter)

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

