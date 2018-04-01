import unittest

from pyFinGraph.sim.Element import Node, Modifier
from pyFinGraph.sim.Event import Event

def main():
    unittest.main()

class SingleEvent_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def test_singleEvent_twoNode_op(self):

        e = Event()

        a = Node("A", init_val = 100)
        b = Node("B")
        mod = Modifier(a,b,100)

        e.subscribe(mod)
        e.subscribe(a)
        e.subscribe(b)

        self.assertTrue(a._val == 100)
        self.assertTrue(b._val == 0)

        e()

        self.assertTrue(a._stage == 0)
        self.assertTrue(a._val == 0)
        self.assertTrue(b._stage == 0)
        self.assertTrue(b._val == 100)

if __name__ == '__main__':
    main()