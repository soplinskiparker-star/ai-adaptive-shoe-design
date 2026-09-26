from flask import Flask
from flask_cors import CORS
from config import get_config
from api.routes import api


def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    CORS(app)
    app.register_blueprint(api, url_prefix="/api")
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=app.config["DEBUG"])
