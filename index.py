from clothes import Pants
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

womans_leather_pants = Pants("Leather Pants", "Slim Fit", 123, "Leather", 50.99, 32, 32, fall, winter, womans)

fall.print()
womans.print()
print(womans_leather_pants)
