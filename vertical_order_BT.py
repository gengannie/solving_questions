from collections import defaultdict
class Solution:
    def __init__(self):
        self.lowest = float('inf')
        self.greatest = float('-inf')
    
    def recurse(self, table, root, row, coln):# time complexity: O(n), 
        # n is the number of nodes in the tree
        if not root:
            return
        if coln < self.lowest:
            self.lowest = coln
        if coln > self.greatest:
            self.greatest = coln
        table[coln].append((row, root.val))
        self.recurse(table, root.left, row + 1, coln - 1)
        self.recurse(table, root.right, row + 1, coln + 1)
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # leftmost column and ending on rightmost column
        # (row, col) 
        # multiple nodes in same row same col, sort node by values
        
        # only coln information matters
        # store each present coln as key and node val into value
        # later sort value, output by smallest key to greatest key
        # first generate the dict using recursion
        ans = []
        table = defaultdict(list)
        self.recurse(table, root, 0, 0)
        for i in range(self.lowest, self.greatest + 1): 
            get_list = table[i]
            if get_list:
                get_list.sort() # time complexity: worst case is O(nlogn) where
                # all of the nodes are in a linear line
                
                ans.append(x[1] for x in get_list)
        return ans
        # how to check for low and max boundary?