import requests

class DeviceCommunication:
    def send_command(self, device_id, command):
        """
        Sends a command to the specified edge device.

        Args:
            device_id (str): Unique identifier for the edge device.
            command (dict): Command to be sent, e.g., {"red_duration": 30, "green_duration": 45}.

        Returns:
            dict: Response from the edge device.
        """
        url = f"http://edge-device-{device_id}/execute"
        try:
            response = requests.post(url, json=command)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

