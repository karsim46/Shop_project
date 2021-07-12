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


