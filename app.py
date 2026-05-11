from flask import Flask
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

# initialize database
db.init_app(app)

# import routes (AFTER db init)
from routes.auth_routes import auth
from routes.patient_routes import patients
from routes.appointment_routes import appointments
from routes.medical_routes import medical
from routes.staff_routes import staff

# register blueprints
app.register_blueprint(auth)
app.register_blueprint(patients)
app.register_blueprint(appointments)
app.register_blueprint(medical)
app.register_blueprint(staff)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # creates SQLite tables automatically
    app.run(debug=True)