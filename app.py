from flask import Flask, render_template

from controllers.vehicles_controller import vehicles_blueprint

app = Flask(__name__)

