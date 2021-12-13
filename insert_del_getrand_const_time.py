from collections import defaultdict
import random
class RandomizedSet:
    def __init__(self):
        self.table = defaultdict()
        self.arr = []
    def insert(self, val):
        # returns true if inserted successfully

        if val in self.table:
            return False
        self.table[val] = len(self.arr) # insert into hashmap is O(1)
        self.arr.append(val) # append into arr is O(1)
        return True
    def remove(self, val):
        if val not in self.table:
            return False
        last_ele, ind = self.arr[-1], self.table[val]
        # remove association between last ind elemetn and ind element
        self.table[last_ele], self.arr[ind] = ind, last_ele
        self.arr.pop() # pop element from array is O(1)
        del self.table[val] # also O(1)
        return True
    def getRandom(self):
        return random.choice(self.arr)
