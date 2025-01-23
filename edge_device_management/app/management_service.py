from app.device_communication import DeviceCommunication

class EdgeDeviceManagementService:
    def __init__(self):
        self.device_comm = DeviceCommunication()

    def execute_command(self, device_id, red_duration, green_duration):
        """
        Sends traffic light timer commands to the edge device.

        Args:
            device_id (str): Unique identifier for the edge device.
            red_duration (int): Duration for the red light.
            green_duration (int): Duration for the green light.

        Returns:
            dict: Response from the edge device.
        """
        command = {
            "red_duration": red_duration,
            "green_duration": green_duration
        }
        return self.device_comm.send_command(device_id, command)