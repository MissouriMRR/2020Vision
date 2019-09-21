import random


class Sampler:
    """
    Sampler for generating data samples

    Parameters
    ----------
    map_size: list(int) size 6
        A min and max value for all rgb values. (min, max, ...)
    """

    def __init__(self, map_size):
        self._enable_iterator = False
        self._iterator = 0

        self.range_min = [map_size[0], map_size[2], map_size[4]]
        self.range_max = [map_size[1], map_size[3], map_size[5]]

    def sample(self, enable_iterator=None):
        """
        Randomly sample each rgb value

        Parameters
        ----------
        enable_iterator: bool, default: None
            Whether to enable the built in iterator to generate values

        Returns
        -------
        Generated int, int, int
        """

        if enable_iterator: self._enable_iterator = enable_iterator

        self._iterator += 1

        def iterator_sample(r_min, r_max):
            return (self._iterator * 25 + r_min) % r_max

        func = iterator_sample if self._enable_iterator else random.randint

        return func(self.range_min[0], self.range_max[0]), func(self.range_min[1], self.range_max[1]), \
               func(self.range_min[2], self.range_max[2])
