# cord tree : binary tree of strings
# leaf node or an internal node
# internal node: left child and right child + length of all children
# leaf node: value and length


# Rope (data structure): composed of smaller strings that is used to efficiently store and manipulate LONG string
# binary tree where leaf node holds a string and length
# each node future up holds the sum of the lengths of all the leaves 
# insert: O(log N)
# index(i) : return character at position i, O(log N)
# recursive search from root node

# much faster insertion and eletion
# don't require O(n) extra memory when operated upon

# greater overall space used when not operated upon
import collections

class ST(object):
	def __init__(self, s):
		self._t = collections.defaultdict(int)
		self._s = s
		self._n = len(s)
		for i in range(self._n):
			self._build(i, 0, self._n-1, 1)

	def _build(self, i, l, r, id):
		if i < l or r < i: return
		if i == l == r:
			self._t[id] = 1
			return
		mid = l + (r-l)/2
		self._build(i, l, mid, id<<1)
		self._build(i, mid+1, r, id<<1|1)
		self._t[id] = self._t[id<<1] + self._t[id<<1|1]

	def delete(self, s, e):
		si, ei = self._find(s+1, 0, self._n-1, 1), self._find(e+1, 0, self._n-1, 1)
		self._update(si, ei, 0, 0, self._n-1, 1)

	def _find(self, s, l, r, id):
		if l==r: return l
		mid = l + (r-l)/2
		if s > self._t[id]: raise Exception('out of range')
		if s > self._t[id<<1]:
			return self._find(s-self._t[id<<1], mid+1, r, id<<1|1)
		return self._find(s, l, mid, id<<1)

	def _update(self, s, e, val, l, r, id):
		if e < l or r < s: return
		if s <= l <= r <= e:
			self._t[id] = val * (r-l+1)
			return
		mid = l + (r-l)/2
		self._update(s, e, val, l, mid, id<<1)
		self._update(s, e, val, mid+1, r, id<<1|1)
		self._t[id] = self._t[id<<1] + self._t[id<<1|1]

	def charAt(self, i):
		idx = self._find(i+1, 0, self._n-1, 1)
		return self._s[idx]

ls = ST("123456789")
ls.delete(0,1)
ls.delete(2,4)
print (ls.charAt(0))
print (ls.charAt(1))
print (ls.charAt(2))
print (ls.charAt(3))

def index (node, ind):
    if node.weight <= ind and node.right:
        return index(node.right, ind - node.weight)
    if node.left:
        return index(node.left, ind)
    return node.data[ind]