from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vehicle import Vehicle
import repositories.vehicle_repository as vehicle_repository
import repositories.manufacturer_repository as manufacturer_repository

vehicles_blueprint = Blueprint("vehicles", __name__)

