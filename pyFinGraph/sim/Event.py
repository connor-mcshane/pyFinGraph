"""
These are the discerte steps taken in the simulation
"""

from datetime import datetime, timedelta

class Event(object):

	def __init__(self, idx):
		self._queue = [[], [], []]

		self._index = idx
		self._nextEvent = None

	@property
	def nextEvent(self):
		return self._nextEvent

	@nextEvent.setter
	def nextEvent(self, value):
		if not(isinstance(value, Event)):
			raise TypeError("Next event must be the same type")
		else:
			self._nextEvent = value

	def subscribe(self, element, priority):
		self._queue[priority].append(element)

	def __call__(self, *args):
		runtime_args = args

		for priority in self._queue:
			for e in priority:
				e.apply(*runtime_args)
		
		return self._nextEvent

class TimeEvent(Event):

	def __init__(self, Timestamp):
		super().__init__(Timestamp)

		if isinstance(Timestamp, datetime):
			self._index = Timestamp
		else:
			raise TypeError("Timesteps require datetime objects")

class Sweep(object):
	""" A sweep is one event repeated over several iterations
	"""

	def __init__(self, event):
		self._base_event = event
		self._cur = 0
		self._indexes = []

	def next(self):

		self._cur += 1

		if self._cur >= len(self._indexes):
			return None
		else:
			return self._indexes[self._cur]

	def __call__(self, *args):
		runtime_args = args
		self._base_event(*runtime_args)

		return self.next()
