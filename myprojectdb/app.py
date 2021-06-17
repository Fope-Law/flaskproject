from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:easy@34.105.152.194:3306/flaskdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) # create SQLALchemy object

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')