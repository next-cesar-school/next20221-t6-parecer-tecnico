from flask import Flask
<<<<<<< HEAD
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB")
=======
app = Flask(__name__)
>>>>>>> 8eef71c08e44933204e6bad3ebe8d9870ab364e0

@app.route('/')
def index():
    return 'Hello World!'

if __name__== '__main__':
    app.run()