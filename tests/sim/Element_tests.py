import unittest
from pyFinGraph.sim.Element import Node, Modifier

def main():
    unittest.main()

class Element_Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_nodeStaging_withHolds_op(self):

        n = Node("test")
        n.stage(100)

        self.assertTrue(n._val == 0)
        self.assertTrue(n._stage == 100)

        n.apply()

        self.assertTrue(n._stage == 0)
        self.assertTrue(n._val == 100)
    
    def test_nodeStaging_noHold_op(self):

        n = Node("test", can_hold=False)
        n.stage(100)

        self.assertTrue(n._val == 0)
        self.assertTrue(n._stage == 100)

        n.apply()

        self.assertTrue(n._stage == 0)
        self.assertTrue(n._val == 0)

    def test_modifierSimple_add_op(self):

        a = Node("A", init_val = 100)
        b = Node("B")

        mod = Modifier(a,b,100)

        self.assertTrue(a._val == 100)
        self.assertTrue(b._val == 0)

        mod.apply()

        self.assertTrue(a._stage == -100)
        self.assertTrue(a._val == 100)
        self.assertTrue(b._stage == 100)
        self.assertTrue(b._val == 0)

        a.apply()
        b.apply()

        self.assertTrue(a._stage == 0)
        self.assertTrue(a._val == 0)
        self.assertTrue(b._stage == 0)
        self.assertTrue(b._val == 100)

if __name__ == '__main__':
    main()