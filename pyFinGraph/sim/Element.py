"""
The Elements. Elements are the smallest units in a model
"""

from abc import ABC, abstractmethod
import logging

class Element(ABC):

    @abstractmethod
    def apply(self):
        pass

    @abstractmethod
    def subscribe_to(self, event):
        pass

class Node(Element):
    """ Nodes are any elements that can either generate/consume
    or hold value.
    """

    def __init__(self, name, init_val=0, can_hold=True):

        self.name = name
        self._val = float(init_val)
        self._can_hold = bool(can_hold)

        self._stage = 0
        self._propotion = 1

    @property
    def val(self):

        if self._can_hold:
            return self._val
        else:
            return self._stage

    def stage(self, value, proportion=0):

        logging.info("Node={};staged={:.2f};proportion={:.2f}".format(self.name, value, proportion))

        if proportion:
            if self._can_hold:
                abs_val = self._val * (proportion/self._propotion)
            else:
                abs_val = self._stage * (proportion/self._propotion)
            self._propotion += proportion
            self._stage += abs_val
            return (-1.0)*abs_val
        else:
            self._stage += value
            return (-1.0)*value

    def subscribe_to(self, event):
        """ Elements that cannot hold value need to apply staging at the end
        of an event
        """

        if self._can_hold:
            event.subscribe(self, 1)
        else:
            event.subscribe(self, 2)

    def apply(self, *args):

        self._propotion = 1

        if self._stage == 0:
            return
        else:
            if (self._can_hold):
                self._val += self._stage
                logging.info("Node={};applied={:.2f};value={:.2f}".format(self.name,
                                                                          self._stage,
                                                                          self._val))
            else:
                logging.warning("Node={};lost={:.2f}".format(self.name,self._stage))

            # Reset staging parameters
            self._stage = 0

class Modifier(Element):
    """ Modifiers change value in nodes over steps. They must subscribe themselves
    and the nodes they modify to the appropriate events
    """

    def __init__(self, src, dst, val, method='add'):

        self._src = src
        self._dst = dst
        self._val = val
        self._method = method

        self.name = "{} to {}".format(self._src.name, self._dst.name)

    def subscribe_to(self, *args):

        for e in args:
            e.subscribe(self, 0)
            self._src.subscribe_to(e)
            self._dst.subscribe_to(e)

    def apply(self, *args):

        if self._method == 'add':
            ret = self._src.stage(-self._val)
            self._dst.stage(ret)

        elif self._method == 'proportion':

            ret = self._src.stage(0, -self._val)
            self._dst.stage(ret)