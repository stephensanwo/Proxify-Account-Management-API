import os
import logging
from flask import Flask, Blueprint
from routes.queries import queries_blueprint
from routes.mutations import mutations_blueprint


app = Flask(__name__)


app.register_blueprint(queries_blueprint)
app.register_blueprint(mutations_blueprint)

if __name__ == '__main__':
    app.run()
