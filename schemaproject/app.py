from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:easy@34.105.152.194:3306/flaskdb' # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) # create SQLALchemy object

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name =  db.Column(db.String(30), nullable=False)

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')