# Scarcity Selector
The Scarcity Selector is a model which aims to have computers 
reproduce how economists make decisions, by attempting to encode
the ideas of opportunity cost and scarcity.  The base class takes is
a comma separated list of arguments (being the target performance for
your competing goals), a learning rate, and a scarcity rate.  It 
encodes this value into an opportunity cost, with a small value being
a good opportunity.