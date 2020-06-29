from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/anusha/Documents/Flaskapp/Flask_App/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False