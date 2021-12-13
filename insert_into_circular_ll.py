class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def insert(head, insertVal): # Node, int -> Node
    if not head:
        new_node = Node(insertVal, None)
        new_node.next = new_node
        return new_node
    prev, curr = head, head.next
    to_insert = False
    while True:
        if prev.val <= insertVal <= curr.val:
            to_insert = True
        elif prev.val > curr.val:
            # tail element located, prev points to tail (largest element)
            if insertVal >= prev.val or insertVal <= curr.val:
                to_insert = True
        if to_insert:
            prev.next = Node(insertVal, curr)
            return head
        prev, curr = curr, curr.next
        if prev == head: # loop condition
            break
    # didn't insert into loop
    prev.next = Node(insertVal, curr)
    return head