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



