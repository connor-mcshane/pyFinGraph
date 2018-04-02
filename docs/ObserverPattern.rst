#########################
Events & Observer Pattern
#########################

We adopt the Oberserver Pattern, where observers subscribe to events.

A simple example is shown below

.. code-block:: python

    e = Event(1)

    a = Node("A", init_val = 100)
    b = Node("B")
    mod = Modifier(a, b, 100)

    mod.subscribe_to(e)
    
    # Step through the event
    e()
    
Here, we have two nodes and a modifier that transfers value between the nodes. 
Alone this collection of elements (one could call a 'model') does nothing.
Only when we introduce events, are there actual cahnges in value observed.

