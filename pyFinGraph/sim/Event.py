"""
These are the discerte steps taken in the simulation
"""

class Event(object):

    def __init__(self):
        pass
        self._nextEvent = None

    @property
    def nextEvent(self):
        """
        Pointer to the next event class
        """

        return self._nextEvent

    @nextEvent.setter
    def nextEvent(self, value):

        if isinstance(value, Event):
            self._nextEvent = value
        else:
            raise TypeError("Next event needs to be an Event type object")