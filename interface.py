"""
Simulate the vision part of the autonomy code.

   sensor data -> vision
				  	| Relevant data
		    		v
drone control <- autonomy
"""
from math import pi
from random import randint

import numpy as np

## TODO
# Better query logic, override conditionals and return bitwise masks?
# Make obstacle distance and or coordinates comparable in numpy arrays

class Obstacle:
	"""
	Watch out.
	"""
	def __init__(self, coords, dimensions):
		self.coords = coords

		self.dimensions = dimensions

	def __gt__(self, value):
		return self.dimensions > value


class Environment:
	"""
	Queriable enviornment data object.
	"""
	def __init__(self):
		self.obs = np.array([])

	def __iter__(self):
		"""
		Generator of all items in environment.
		* Does not reset when observation is updated *
		
		? Make enumerate friendly.
		"""
		i = 0
		while True:
			yield self.obs[i]

			i = (i + 1) % len(self.obs) 

	def __getitem__(self, query):
		"""
		Process query
		
		Parameters
		----------
		query: int/iterable/str
			Index / Mask / Conditional

		Returns
		-------
		Values fitting query.
		"""
		try:
			if isinstance(query, (int, float)):
				# if is indexing a specific value
				return self.obs[query]
				
			elif isinstance(query, (list, tuple, dict)):
				# if is a mask
				return self.obs[np.where(query)]
				
			elif isinstance(query, (str)):
				# if is conditional
				return self.obs[np.where(eval(query))]
		except IndexError:
			return None

	def update(self, observation):
		"""
		Update observed environment.
		"""
		self.obs = np.array(observation)


if __name__ == '__main__':
	env = Environment()

	env.update([Obstacle((randint(0, 2*pi // 1), randint(0, 100)), i) for i in range(5)])

	print(env['self.obs > 3'])

	i = (v for v in env)

	print(next(i))

	env.update(['test', 'test2'])

	print(next(i))
	print(next(i))
	print(next(i))
	env.update(['test', 'test2', 'test3'])
	print(next(i))
