"""
These are the discerte steps taken in the simulation
"""

from datetime import datetime

class Event(object):

	def __init__(self, *args):
		self._elements = list()
		self.args = args

		self._nextEvent = None

	@property
	def nextEvent(self):
		return self._nextEvent

	@nextEvent.setter
	def nextEvent(self, value):
		if not(isinstance(value, self)):
			raise TypeError("Next event must be the same type")
		else:
			self._nextEvent = value

	def subscribe(self, element):
		self._elements.append(element)

	def __call__(self, *args):
		runtime_args = self.args + args
		for ele in self._elements:
			ele.apply(*runtime_args)

class TimeEvent(Event):

	def __init__(self, Timestamp, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if isinstance(Timestamp, datetime):
			self._index = Timestamp
		else:
			raise TypeError("Timesteps require datetime objects")