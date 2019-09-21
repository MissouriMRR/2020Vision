class AccuracyTracker:
    """
    Stores historical accuracy values to generate accuracy metrics
    """
    def __init__(self, data=None):
        self.data = data if data else []

    def __add__(self, value):
        """
        Adds calcuted value too data

        Parameters
        ----------
        value: bool
            Value to be added to accuracy_tracker
        """

        return AccuracyTracker(self.data + [value])

    def add(self, prediction, choice):
        """
        Add too data and have do comparison for you

        Parameters
        ----------
        prediction: Possible category
            The predicted value
        choice: Possible category
            The chosen value
        """

        self.data.append((prediction == choice))

    @property
    def accuracy(self):
        """
        Calculates past accuracy for up to 20 moves

        Returns
        -------
        -1 if no items in past accuracy else accuracy as int
        """

        if not self.data:
            return -1

        iterations = min(20, len(self.data))

        num_correct = sum([row for row in self.data[-iterations:]])

        return (num_correct * 100) // iterations
