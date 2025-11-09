from flask import Flask
from flask_cors import CORS
from routes.companies import companies_bp
from routes.devices import devices_bp

app = Flask(__name__)
CORS(app)

# API routes
app.register_blueprint(companies_bp)
app.register_blueprint(devices_bp)

@app.route('/')
def index():
    return "Flask backend is running successfully!"

if __name__ == '__main__':
    app.run(debug=True)
