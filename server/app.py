#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import (
    Flask,
    request,
    g,
    session,
    json,
    jsonify,
    render_template,
    make_response,
    url_for,
    redirect,  # this is not necessary as react router handles redirects
)

# imports
from flask_restful import Api, Resource
from time import time
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)  # instantiate new instance of Api class


# Views go here!
# the Products class is not your model, but a new class that represents the information you will be accessing
class Products(Resource):
    # self is the instance of the class
    def get(self):
        # the as_dict() method that you built in models is used here b/c you can only serialize if it is converted to a dictionary
        products = [product.as_dict() for product in Products.query.all()]

        # you can also just 'return products, 200' but make_response is preferred
        return make_response(products, 200)


class Profile(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


# api.add_resource() tells the api to look at a specified resource (connects to resource);
# 1st arg: which resource you're adding, 2nd arg: the endpoint
api.add_resource(Products, "/products")
api.add_resource(Customer, "/customer")
api.add_resource(Orders, "/orders")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
