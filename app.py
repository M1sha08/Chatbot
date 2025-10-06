from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
  app = Flask(__name__, template_folder="templates", static_folder="static")

  from routes import register_routes
  register_routes(app)

  return app