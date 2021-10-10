# Difference between HashMap and TreeMap

## Hashmap (Dictionary)

- using hasing algorithm implementation
- get, put: O(1) (asssuming hash function disperses elements evenly)
- allows one null value
- fast
- suitable if not requirement of sorting


## Ordered Dicitonary 
- inserted keys in order 
- "from collections import OrderedDict"
- od = OrderedDict()
- If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.
- od.pop("key")