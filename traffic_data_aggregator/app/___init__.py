from flask import Flask
from .database import db  # Import the database instance
from .routes import main   # Import the routes defined in routes.py

def create_app():
    """
    Initialize the Flask application.
    
    This function sets up the app configuration, database, and registers 
    the blueprint for handling routes.
    
    Returns:
        app (Flask): The initialized Flask application.
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration settings

    db.init_app(app)  # Initialize the database with the app
    app.register_blueprint(main)  # Register the main blueprint with the app
    return app