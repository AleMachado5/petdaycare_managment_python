from flask import Flask
from controllers.pets_controller import pets_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(pets_bp, url_prefix="/api/pets")

if __name__ == "__main__":
    app.run(debug=True)