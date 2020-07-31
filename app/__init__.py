import os
import rq
from flask import Flask, request, current_app
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.remderpage import bp as remderpage_bp
    app.register_blueprint(remderpage_bp)


    return app