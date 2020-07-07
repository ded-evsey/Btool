from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .settings import conf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conf['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()

