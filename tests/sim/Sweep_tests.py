import unittest

from pyFinGraph.sim.Element import Node, Modifier
from pyFinGraph.sim.Event import Event, Sweep

def main():
    unittest.main()

class Sweep_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_SweepBasic_ManualIdxAdd_nop(self):
        """ Here we don't have to make several events to which
        each element must subscribe to. Instead, we only make one
        base event, and re-use that event over a Sweep object
        """

        A = Node("A")
        B = Node("B")
        M = Modifier(A, B, 1)

        e = Event(1)
        M.subscribe_to(e)

        s = Sweep(e)

        #This won't happen in actual code, but for TDD purposes
        #we will extend the list like this
        s._indexes.extend([1,2,3])

        self.assertTrue(A.val == 0)
        self.assertTrue(B.val == 0)

        ret = 0
        while ret is not None:
            ret = s()

        self.assertTrue(A.val == -B.val)
        self.assertTrue(B.val == 3)

if __name__ == '__main__':
    main()