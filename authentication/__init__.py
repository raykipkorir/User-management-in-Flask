from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SECRET_KEY"] = "a5583a03fe5cfe981bfda5b3"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///core.db"

flask_bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from authentication import routes
