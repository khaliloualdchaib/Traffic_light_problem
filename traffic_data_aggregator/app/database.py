from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # Import datetime module for timestamps

# Initialize the SQLAlchemy instance for ORM
db = SQLAlchemy()

class TrafficData(db.Model):
    """
    Model representing traffic data at a traffic light.
    
    Attributes:
        id (int): Primary key for the TrafficData entry.
        traffic_light_id (str): Identifier for the traffic light.
        num_cars (int): Number of cars at the traffic light.
        num_pedestrians (int): Number of pedestrians at the traffic light.
        timestamp (datetime): The time at which the data was recorded.
    """
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    traffic_light_id = db.Column(db.String, nullable=False)  # Unique ID for each traffic light
    num_cars = db.Column(db.Integer, nullable=False)  # Count of cars passing
    num_pedestrians = db.Column(db.Integer, nullable=False)  # Count of pedestrians
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Timestamp for the entry

    def _repr_(self):
        """Return a string representation of the TrafficData instance."""
        return f'<TrafficData {self.traffic_light_id} at {self.timestamp}>'