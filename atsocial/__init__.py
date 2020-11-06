from flask import Flask
app = Flask(__name__)

from atsocial.views import views
app.register_blueprint(views)

from atsocial.error_pages.handlers import error_pages
app.register_blueprint(error_pages)