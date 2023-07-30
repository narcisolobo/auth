from flask import Blueprint

main = Blueprint("main", __name__)

from factory.blueprints.main import routes
