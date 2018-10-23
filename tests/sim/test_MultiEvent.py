import unittest

from pyFinGraph.sim.Element import Node, Modifier
from pyFinGraph.sim.Event import Event

def main():

    unittest.main()

class SingleEvent_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def test_twoEvents_ManualSub_Op(self):
        
        e = Event(1)
        e2 = Event(2)
        e.nextEvent = e2

        NetInput = Node("Net Input")
        src = Node("src", can_hold=False)
        a = Node("A1")
        b = Node("B1")

        mod0 = Modifier(NetInput, src, 200)
        mod1 = Modifier(src, a, 0.50, method='proportion')
        mod2 = Modifier(src, b, 0.50, method='proportion')

        mod0.subscribe_to(e, e2)
        mod1.subscribe_to(e, e2)
        mod2.subscribe_to(e, e2)

        self.assertTrue(NetInput._val == 0)
        self.assertTrue(src._val == 0)
        self.assertTrue(a._val == 0)
        self.assertTrue(b._val == 0)

        e = e()

        self.assertTrue(NetInput._val == -200)
        self.assertTrue(src._val == 0)
        self.assertTrue(a._val == 100)
        self.assertTrue(b._val == 100)

        e = e()

        self.assertTrue(NetInput._val == -400)
        self.assertTrue(src._val == 0)
        self.assertTrue(a._val == 200)
        self.assertTrue(b._val == 200)

        self.assertTrue(e is None)

if __name__ == '__main__':
    main()