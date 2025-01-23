from app.dqn_model import DQNModel

class TrafficOptimizationService:
    def __init__(self, model_path):
        self.dqn_model = DQNModel(model_path)

    def get_optimized_timers(self, num_cars, num_pedestrians, time_of_day):
        """
        Get optimized traffic light timers.

        Args:
            num_cars (int): Number of cars at the intersection.
            num_pedestrians (int): Number of pedestrians at the intersection.
            time_of_day (float): Time of day in hours.

        Returns:
            dict: Dictionary containing red and green light durations.
        """
        state = [num_cars, num_pedestrians, time_of_day]
        red_duration, green_duration = self.dqn_model.predict(state)
        return {"red_duration": red_duration, "green_duration": green_duration}