from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vehicle import Vehicle
from models.manufacturer import Manufacturer
import repositories.vehicle_repository as vehicle_repository
import repositories.manufacturer_repository as manufacturer_repository

vehicles_blueprint = Blueprint("vehicles", __name__)

@vehicles_blueprint.route("/vehicles")
def vehicles():
    vehicles = vehicle_repository.select_all() 
    return render_template("vehicles/index.html", all_vehicles = vehicles)

#NEW
# GET '/vehicles/new'
@vehicles_blueprint.route("/vehicles/new", methods=['GET'])
def new_vehicle():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/vehicles/new.html", all_manufacturers = manufacturers)

#create 
#POST '/vehicles'
@vehicles_blueprint.route("/vehicles", methods=['POST'])
def create_vehicle():
    description = request.form['description']
    engine = request.form['engine']
    gearbox = request.form['gearbox']
    colour = request.form['colour']
    price = request.form['price']
    year = request.form['year']
    quantity = request.form['quantity']
    for_sale = request.form['for_sale']
    make = request.form['make']
    image = request.form['image']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    vehicle = Vehicle(description, engine, gearbox, colour, price, year, quantity, for_sale, manufacturer, make, image )
    vehicle_repository.save(vehicle)
    return redirect('/vehicles')

# SHOW
# GET '/vehicles/<id>'
@vehicles_blueprint.route("/vehicles/<id>", methods=['GET'])
def show_vehicle(id):
    vehicle = vehicle_repository.select(id)
    return render_template('vehicles/show.html', vehicle = vehicle)

# EDIT
# GET '/vehicles/<id>/edit'
@vehicles_blueprint.route("/vehicles/<id>/edit", methods=['GET'])
def edit_vehicle(id):
    vehicle = vehicle_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('vehicles/edit.html', vehicle = vehicle, all_manufacturers = manufacturers)

# UPDATE
# PUT '/vehicles/<id>'
@vehicles_blueprint.route("/vehicles/<id>", methods=['POST'])
def update_vehicle(id):
    description = request.form['description']
    engine = request.form['engine']
    gearbox = request.form['gearbox']
    colour = request.form['colour']
    price = request.form['price']
    year = request.form['year']
    quantity = request.form['quantity']
    for_sale = request.form['for_sale']
    make = request.form['make']
    image = request.form['image']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    vehicle = Vehicle(description, engine, gearbox, colour, price, year, quantity, for_sale, manufacturer, make, image, id)
    #req help relating to class
    print(vehicle.display_name())
    vehicle_repository.update(vehicle)
    return redirect('/vehicles')

# DELETE
# DELETE '/vehicles/<id>'
@vehicles_blueprint.route("/vehicles/<id>/delete", methods=['POST'])
def delete_vehicle(id):
    vehicle_repository.delete(id)
    return redirect('/vehicles')










