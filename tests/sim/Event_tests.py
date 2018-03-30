import unittest

from pyFinGraph.sim.Event import Event

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

        a = Event()
        b = Event()

        with self.assertRaises(TypeError):
            a.nextEvent = 2

if __name__ == '__main__':
    main()
