#######
Classes
#######

Overall, there are four core base classes:

+ Elements
+ Events
+ Models
+ Scenarios

Elements and events are considered the 'primitive' classes of the entire suite.

A collection of elements makes a model, and a collection of events make a horizon.

A scenario is a model with one or more horizons. This design allows users to re-use
models for various scenarios and compare the differences.

Elements
========

Elements are those which handle value; they can either store value (holding nodes), 
generate/consume value (Non-holding nodes), or modify value (Modifiers) - either by
transferring value from node to node, or by adjusting value