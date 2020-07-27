from flask import Flask
from flask_login import LoginManager
from flask_caching import Cache
import logging
import os.path

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.path.isfile(os.path.join(BASE_DIR, 'config_prod.py')):
    app.config.from_object('config_prod')
else:
    app.config.from_object('config')

cache = Cache(app)

handler = logging.StreamHandler()
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

# Security
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from juntos import views, models

