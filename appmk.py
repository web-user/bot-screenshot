from datetime import timedelta
from app import create_app
from flask_script import Manager, Shell, Server


app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()