from flask import Flask
import os
from flasgger import Swagger
from waitress import serve

from src.database import db

from src.config.swagger import template, swagger_config
from src.student import studentBlueprint

app = Flask(__name__,instance_relative_config=True)
app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SWAGGER={
                'title': "College Student APIs",
                'uiversion': 3
            }
        )

db.app = app
db.init_app(app)
app.register_blueprint(studentBlueprint)
serve(app, host='127.0.0.1', port=8087)  # Replace the host and port with your desired values
Swagger(app, config=swagger_config, template=template)
