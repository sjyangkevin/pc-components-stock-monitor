from flask import Flask
from flaskr import db
from flaskr import index

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    db.init_app(app)

    app.register_blueprint(index.bp)

    return app