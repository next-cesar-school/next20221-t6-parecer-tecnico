from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB")

@app.route('/')
def index():
    return 'Hello World!'

if __name__== '__main__':
    app.run()