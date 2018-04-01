import unittest
from datetime import datetime

from pyFinGraph.sim.Event import Event, TimeEvent

def main():
    unittest.main()

class Event_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_nextEventProperty_inputValidation_nop(self):
        """
        Test the next event link is correctly type
        checked
        """

        a = Event(1)
        b = Event(2)

        with self.assertRaises(TypeError):
            a.nextEvent = 2

    def test_TimeEvent_InitInputValidation_Nop(self):

        with self.assertRaises(TypeError):
            a = TimeEvent(2)
            
        b = TimeEvent(datetime(2012,1,1))

    def test_TimeEvent_Ordering_Op(self):

        a = TimeEvent(datetime(2012,1,1))
        b = TimeEvent(datetime(2013,1,1))
        l = [b, a]

        l.sort(key=lambda x: x._index)

        self.assertTrue(l[0] == a)

if __name__ == '__main__':
    main()
