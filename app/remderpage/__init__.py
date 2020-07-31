from flask import Blueprint

bp = Blueprint('remderpage', __name__)

from app.remderpage import routes