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


