import sys
from flask import Flask

sys.path.append('../config')

api = Flask(__name__)
api.config.from_object('config.app.ConfigApp')