import pdb
from models.vehicle import Vehicle
from models.manufacturer import Manufacturer

import repositories.vehicle_repository as vehicle_repository
import repositories.manufacturer_repository as manufacturer_repository

vehicle_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("Delorean")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Dodge")
manufacturer_repository.save(manufacturer2)

vehicle1 = Vehicle("DMC", 3.0, "manual", "Aluminium", 30000, 1985, 1, True, manufacturer1)
vehicle_repository.save(vehicle1)

vehicle2 = Vehicle("Charger", 5.0, "Automatic", "Orange", 49000, 1979,1,True,manufacturer2)
vehicle_repository.save(vehicle2)



