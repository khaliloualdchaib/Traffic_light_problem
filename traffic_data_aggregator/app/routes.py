from flask import Blueprint, request, jsonify
from .database import db, TrafficData
import datetime

# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

@main.route('/submit_data', methods=['POST'])
def submit_data():
    """
    Endpoint to submit traffic data for a traffic light.
    
    Expects a JSON payload with:
        - traffic_light_id: ID of the traffic light
        - num_cars: Number of cars at that light
        - num_pedestrians: Number of pedestrians at that light
        - timestamp: The time of data collection (optional, defaults to current time)
      
    Returns:
        JSON response indicating success or error message.
    """
    data = request.json
    try:
        timestamp = data.get('timestamp', datetime.utcnow())  # Get timestamp or use the current time
        if isinstance(timestamp, str):
            # Convert the timestamp from string to datetime
            timestamp = datetime.fromisoformat(timestamp)

        # Create a new TrafficData instance with the submitted data
        traffic_data = TrafficData(
            traffic_light_id=data['traffic_light_id'],
            num_cars=data['num_cars'],
            num_pedestrians=data['num_pedestrians'],
            timestamp=timestamp  # Set the timestamp
        )
        
        db.session.add(traffic_data)  # Add the new instance to the session
        db.session.commit()  # Commit changes to the database
        
        return jsonify({"message": "Data submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return error message if something goes wrong

@main.route('/traffic_data', methods=['GET'])
def get_traffic_data():
    """
    Endpoint to retrieve all traffic data from the database.
    
    Returns:
        JSON response with a list of all TrafficData entries.
    """
    all_data = TrafficData.query.all()  # Query all entries in TrafficData
    return jsonify([{
        "traffic_light_id": d.traffic_light_id,
        "num_cars": d.num_cars,
        "num_pedestrians": d.num_pedestrians,
        "timestamp": d.timestamp.isoformat()  # Convert timestamp to ISO format for JSON serialization
    } for d in all_data]), 200  # Return list of traffic data