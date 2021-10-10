#leetcode solution versus mine, mine assumes root node must be crossed, but this is not true
diameter = 0

def longest_path(node):
    if not node:
        return 0
    nonlocal diameter
    # recursively find the longest path in
    # both left child and right child
    left_path = longest_path(node.left)
    right_path = longest_path(node.right)

    # update the diameter if left_path plus right_path is larger
    diameter = max(diameter, left_path + right_path)

    # return the longest one between left_path and right_path;
    # remember to add 1 for the path connecting the node and its parent
    return max(left_path, right_path) + 1

longest_path(root)
return diameter
#LEETCODE solution below:

diameter = 0

def longest_path(node):
    if not node:
        return 0
    nonlocal diameter
    # recursively find the longest path in
    # both left child and right child
    left_path = longest_path(node.left)
    right_path = longest_path(node.right)

    # update the diameter if left_path plus right_path is larger
    diameter = max(diameter, left_path + right_path)

    # return the longest one between left_path and right_path;
    # remember to add 1 for the path connecting the node and its parent
    return max(left_path, right_path) + 1

longest_path(root)
print(diameter) 