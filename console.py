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

vehicle1 = Vehicle("Delorean", 3.0, "Manual", "Stainless", 30000, 1985, 1, True, manufacturer1,"DMC","https://www.capitalgazette.com/resizer/ZgUELyLTV0LXJVV2zqapUqlhKCk=/800x600/top/cloudfront-us-east-1.images.arcpublishing.com/tronc/3YSQHFDPWVGKVLSMMOJQWZKCUM.jpg")
vehicle_repository.save(vehicle1)

vehicle2 = Vehicle("Charger", 5.0, "Automatic", "Orange", 49000, 1979, 1,True, manufacturer2,"Dodge","https://s1.cdn.autoevolution.com/images/news/80k-1969-dodge-charger-is-a-general-lee-clone-153739_1.jpg")
vehicle_repository.save(vehicle2)



