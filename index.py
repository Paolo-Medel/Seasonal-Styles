from clothes import Pants, Shirt, Socks, Sweater, Undies
from seasons import Hot_Weather, Cold_Weather, Cool_Weather
from department import Departments

summer = Hot_Weather("Summer")
fall = Cool_Weather("Fall")
spring = Cool_Weather("Spring")
winter = Cold_Weather("Winter")

mens = Departments("Mens", "Front-Left")
womans = Departments("Womans", "Front-Left")
children = Departments("Children", "Front-Left")
young_adults = Departments("young adults", "Front-Left")

womans_leather_pants = Pants("Leather Pants", "Slim Fit Faux Leather", 123, "Faux Leather", 50.99, 32, 32, fall, winter, womans)
mens_stripped_shirt = Shirt("Stripped Shirt", "Slim Fit", 231, "Cotton", 25.99, "Medium", True, summer, spring, mens)


summer.print()
mens.print()
print(mens_stripped_shirt)

#I need to be able to add a range of sizes