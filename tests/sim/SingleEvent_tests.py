import unittest
import logging, sys

from pyFinGraph.sim.Element import Node, Modifier
from pyFinGraph.sim.Event import Event

def main():
    logger = logging.getLogger('foo')
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.INFO)

    unittest.main()

class SingleEvent_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def test_twoNodeNoSource_ManualSub_Op(self):

        e = Event(1)

        a = Node("A", init_val = 100)
        b = Node("B")
        mod = Modifier(a,b,100)

        mod.subscribe_to(e)

        self.assertTrue(a._val == 100)
        self.assertTrue(b._val == 0)

        e()

        self.assertTrue(a._stage == 0)
        self.assertTrue(a._val == 0)
        self.assertTrue(b._stage == 0)
        self.assertTrue(b._val == 100)

    def test_twoNodeOneSource_ManualSub_Op(self):
        
        e = Event(1)

        NetInput = Node("Net Input")
        src = Node("src", can_hold=False)
        a = Node("A1")
        b = Node("B1")

        mod0 = Modifier(NetInput, src, 200)
        mod1 = Modifier(src, a, 0.50, method='proportion')
        mod2 = Modifier(src, b, 0.50, method='proportion')

        mod0.subscribe_to(e)
        mod1.subscribe_to(e)
        mod2.subscribe_to(e)

        self.assertTrue(NetInput._val == 0)
        self.assertTrue(src._val == 0)
        self.assertTrue(a._val == 0)
        self.assertTrue(b._val == 0)

        e()

        self.assertTrue(NetInput._val == -200)
        self.assertTrue(src._val == 0)
        self.assertTrue(a._val == 100)
        self.assertTrue(b._val == 100)

if __name__ == '__main__':
    main()