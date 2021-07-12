from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vehicle import Vehicle
import repositories.vehicle_repository as vehicle_repository
import repositories.manufacturer_repository as manufacturer_repository

vehicles_blueprint = Blueprint("vehicles", __name__)

@vehicles_blueprint.route("/vehicles")
def vehicles():
    vehicles = vehicle_repository.select_all() 
    return render_template("vehicles/index.html", all_vehicles = vehicles)

#create 
#POST '/vehicles'
@vehicles_blueprint.route("/vehicles", methods =['POST'])
def create_vehicles():
    description = request.form['description']
    engine = request.form['engine']
    gearbox = request.form['gearbox']
    colour = request.form['colour']
    price = request.form['price']
    year = request.form['year']
    quantity = request.form['quantity']
    for_sale = request.form['for_sale']
    manufacturer = manufacturer_repository.select(request.form['manufacturer.id'])
    vehicle = Vehicle(description, engine, gearbox, colour, price, year, quantity, for_sale, manufacturer)
    vehicle_repository.save(vehicle)
    return redirect('/vehicles')
