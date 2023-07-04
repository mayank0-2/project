from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@127.0.0.1:3306/Basic_Flask'

db = SQLAlchemy(app)
migrate = Migrate(app, db)  #resource used to implement migration https://pypi.org/project/Flask-Migrate/

class Data(db.Model):   #model for the database
    # __tablename__ = 'data'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = True)
    college = db.Column(db.String(100))
    
    def __init__(self, name, college):
        self.name = name
        self.college = college
        
