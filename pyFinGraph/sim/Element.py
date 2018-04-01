"""
The Elements. Elements are the smallest units in a model
"""

from abc import ABC, abstractmethod

class Element(ABC):

    @abstractmethod
    def apply(self):
        pass

class Node(Element):
    """ Nodes are any elements that can either generate/consume
    or hold value.
    """

    def __init__(self, name, init_val=0, can_hold=True):

        self.name = name
        self._val = float(init_val)
        self._stage = 0
        self._can_hold = can_hold

    def stage(self, value):
        self._stage += value

    def apply(self, *args):
        if self._stage == 0:
            return
        else:

            if (self._can_hold):
                self._val += self._stage
                print("{}:\tSTAGED={:.2f}\tEND={:.2f}".format(self.name, self._stage, self._val))#TEST
            else:
                print("Element cannot hold value, {:.2f} lost from model".format(self._stage))

            self._stage = 0

class Modifier(Element):
    """ Modifiers change value in nodes over steps. They must subscribe themselves
    and the nodes they modify to the appropriate events
    """

    def __init__(self, src, dst, val, method='add'):

        if src is None:
            self._src = solver.input
        else:
            self._src = src

        if dst is None:
            self._dst = solver.output
        else:
            self._dst = dst

        self._name = "{} to {}".format(self._src.name, self._dst.name)

        self._val = val

        self._method = method

    def apply(self, *args):

        if self._method == 'add':
            self._src.stage(-self._val)
            self._dst.stage(self._val)

        elif self._method == 'proportion':
            add_val = self._val * self._src._val
            self._dst.stage(add_val)
            self._src.stage(-add_val)