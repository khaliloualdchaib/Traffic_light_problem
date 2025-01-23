from flask import Flask, request, jsonify
from app.management_service import EdgeDeviceManagementService

app = Flask(__name__)
service = EdgeDeviceManagementService()

@app.route('/send_command', methods=['POST'])
def send_command():
    """
    API endpoint to send traffic light commands to an edge device.

    Expects JSON payload with:
        - device_id: ID of the edge device.
        - red_duration: Duration for the red light.
        - green_duration: Duration for the green light.

    Returns:
        JSON response with the device's acknowledgment or error message.
    """
    data = request.json
    device_id = data.get('device_id')
    red_duration = data.get('red_duration')
    green_duration = data.get('green_duration')

    if not device_id or red_duration is None or green_duration is None:
        return jsonify({"error": "Missing required parameters."}), 400

    response = service.execute_command(device_id, red_duration, green_duration)
    return jsonify(response), 200
