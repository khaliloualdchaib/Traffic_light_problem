from flask import Flask, request, jsonify
from app.optimization_service import TrafficOptimizationService

app = Flask(__name__)
service = TrafficOptimizationService(model_path="path_to_pretrained_model.pth")

@app.route('/optimize', methods=['POST'])
def optimize():
    """
    API endpoint to optimize traffic light timers.

    Expects JSON payload with:
        - num_cars: Number of cars at the intersection.
        - num_pedestrians: Number of pedestrians at the intersection.
        - time_of_day: Current time in hours.

    Returns:
        JSON response with optimized red and green light durations.
    """
    data = request.json
    num_cars = data.get('num_cars')
    num_pedestrians = data.get('num_pedestrians')
    time_of_day = data.get('time_of_day')

    if num_cars is None or num_pedestrians is None or time_of_day is None:
        return jsonify({"error": "Missing required parameters."}), 400

    timers = service.get_optimized_timers(num_cars, num_pedestrians, time_of_day)
    return jsonify(timers), 200