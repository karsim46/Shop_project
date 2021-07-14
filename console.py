import pdb
from models.vehicle import Vehicle
from models.manufacturer import Manufacturer

import repositories.vehicle_repository as vehicle_repository
import repositories.manufacturer_repository as manufacturer_repository

vehicle_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("DMC")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Dodge")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer("Pontiac")
manufacturer_repository.save(manufacturer3)

vehicle1 = Vehicle("Delorean", 2.8, "Manual", "Stainless", 38000, 1985, 1, True, manufacturer1,"DMC","https://www.capitalgazette.com/resizer/ZgUELyLTV0LXJVV2zqapUqlhKCk=/800x600/top/cloudfront-us-east-1.images.arcpublishing.com/tronc/3YSQHFDPWVGKVLSMMOJQWZKCUM.jpg")
vehicle_repository.save(vehicle1)

vehicle2 = Vehicle("Charger", 5.7, "Automatic", "Orange", 49335, 1969, 1,True, manufacturer2,"Dodge","https://s1.cdn.autoevolution.com/images/news/80k-1969-dodge-charger-is-a-general-lee-clone-153739_1.jpg")
vehicle_repository.save(vehicle2)

vehicle3 = Vehicle("Transam", 6.5, "Automatic", "Black", 63000, 1982, 1, True, manufacturer3, "Pontiac","https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/K.I.T.T._Nachbau_aus_Deutschland.jpg/800px-K.I.T.T._Nachbau_aus_Deutschland.jpg")
vehicle_repository.save(vehicle3)

