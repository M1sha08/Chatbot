from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
  app = Flask(__name__, template_folder="templates", static_folder="static")

  basedir = os.path.abspath(os.path.dirname(__file__))
  app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'chats.db')

  db.init_app(app)
  migrate.init_app(app, db) # UNSURE

  from routes import register_routes
  register_routes(app)

  return app