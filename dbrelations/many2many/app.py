from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref 

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:easy@34.105.152.194:3306/many2many' # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) 

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    purchase = db.relationship('Purchases', backref='customer')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    purchase = db.relationship('Purchases', backref='product')

class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customers_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0') 
