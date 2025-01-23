import os

class Config:
    """
    Configuration settings for the Flask application.
    
    Attributes:
        SQLALCHEMY_DATABASE_URI (str): URI for the database connection.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disable track modifications to save resources.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///traffic_data.db')  # Default to SQLite if no DB URL provided
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for efficiency

    