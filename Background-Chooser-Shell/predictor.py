"""
K nearest neighbors predictor
"""

class Predictor:
    """
    Generates prediction based on historical data
    """
    def __init__(self, historical_data=[]):
        self.historical_data = historical_data
        self.accuracy_tracker = []

    def predict(self, color):
        """
        Uses nearest neighbor(s) to predict most probable output for given color

        Parameters
        ----------
        color: (int, int, int)
            Color to classify

        Returns
        -------
        'w' or 'b'
        """
        import numpy as np

        # TODO your code here
        # use self.historical_data: [((red, green, blue), user_choice), ...]
        # to choose 'w' or b'
        # Euclidean distances of this data point to all in dataset

        # for (r, g, b), choice in self.historical_data:

        return np.random.choice(['w', 'b'])
