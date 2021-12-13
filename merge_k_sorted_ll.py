# merge two sorted linked lists
# given heads of two sorted linked lists, merge the two lists in one sorted lists

# approach 1: recursion
# time: O(n + m), where n is length of first list and m is length of second list
# space: O(n + m): stack frames

# approach 2: iteration
# time: O(n + m)
# space: O(1)
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def merge_two_sorted_ll(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_sorted_ll(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_ll(l1, l2.next)
        return l2

def iterative_approach(l1, l2):
    # 1 -> 2 -> 3

    # 3 -> 5
    # 1 -> 2 -> 4

    # account for cases when either/noth of them is None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    prev = sentinel = ListNode(0)
    while l1 is not None and l2 is not None:
        if l1.val < l2.val: # l1 is the smaller element
            # increment l1, let prev.next be l1
            prev.next = l1
            prev = l1
            l1 = l1.next
        else: # l2 has the smaller element
            prev.next = l2
            prev = l2
            l2 = l2.next
            

    if l1 is not None:
        prev.next = l1
    elif l2 is not None:
        prev.next = l2
