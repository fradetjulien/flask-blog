from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e27b684eb7da909db44f70814bae62a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site-db'
db = SQLAlchemy(app)

from flaskblog import routes
