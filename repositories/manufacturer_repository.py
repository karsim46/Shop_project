from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.vehicle import Vehicle

# Manufacture save function added
def save(manufacturer):
    sql = "INSERT INTO manufacturers(make) VALUES (%s) RETURNING *"
    values = [manufacturer.make]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

# Select all function for manufacturers list
def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['make'], row['id'] )
        manufacturers.append(manufacturer)
    return manufacturers

# Select one manufacturer from list
def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['make'], result['id'])
        return manufacturer

# Delete all manufacturer function created
def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

#Delete one manufacturer from list
def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update manufacturer function
def update(manufacturer):
    sql = "UPDATE manufacturers SET (make) = (%s) WHERE id = %s"
    values = [manufacturer.make, manufacturer.id]
    run_sql(sql, values)

# add manufacturers to vehicles list
def vehicles(manufacturer):
    vehicles = []

    sql = "SELECT * FROM vehicles WHERE manufacturer.id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        vehicle = Vehicle(row['description'], row['engine'], row['gearbox'], row['colour'], row['price'], row['year'], row['quantity'], row['for_sale'], row['manufacturer.id', row['id']])
        vehicles.append(vehicle)
    return vehicles









