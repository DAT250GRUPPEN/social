from flask import Flask
app = Flask(__name__)

import atsocial.views
#from atsocial.error_pages.handlers

#app.register_blueprint(error_pages)