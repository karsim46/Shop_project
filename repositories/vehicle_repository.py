from db.run_sql import run_sql

from models.vehicle import Vehicle
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

# save feature for being able to add a  vehicle to repo.
def save(vehicle):
    sql = "INSERT INTO vehicles (description, engine, gearbox, colour, price, year, quantity, for_sale, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [vehicle.description, vehicle.engine, vehicle.gearbox, vehicle.colour, vehicle.price, vehicle.year, vehicle.quantity, vehicle.for_sale, vehicle.manufacturer_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    vehicle.id = id
    return vehicle
# select all feature displaying all inventory.
def select_all():
    vehicles = []

    sql = "SELECT * FROM vehicles"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        vehicle = Vehicle(row['description'], row['engine'], row['gearbox'], row['colour'], row['price'], row['year'], row['quantity'], row['for_sale'], manufacturer, row['id'])
        vehicles.append(vehicle)
    return vehicles

# select one feature allowing user to select one vehicle by id(determined by database).
def select(id):
    vehicle = None
    sql = "SELECT * FROM vehicles WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        vehicle = Vehicle(result['description'], result['engine'], result['gearbox'], result['colour'], result['price'], result['year'], result['quantity'], result['for_sale'], manufacturer, result['id'])
        return vehicle

