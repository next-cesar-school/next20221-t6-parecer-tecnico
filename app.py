from unicodedata import name
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB")

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello World!'

if __name__== '__main__':
    app.run()