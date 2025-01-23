import torch

class DQNModel:
    def __init__(self, model_path):
        self.model = torch.load(model_path)
        self.model.eval()

    def predict(self, state):
        """
        Predict optimal action based on the current state.

        Args:
            state (list): The input state [num_cars, num_pedestrians, time_of_day].

        Returns:
            list: Optimal red and green light durations.
        """
        with torch.no_grad():
            state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
            action = self.model(state_tensor).squeeze(0).tolist()
        return action
    