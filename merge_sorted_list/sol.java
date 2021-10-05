class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
n_1 = ListNode (1)
n_2 = ListNode (2)
n_3 = ListNode (3)
n_4 = ListNode (4)
n_5 = ListNode (5)
n_6 = ListNode (6)
l1 = n_1
l1.next = n_3
n_3.next = n_5

l2 = n_2
n_2.next = n_4
n_4.next = n_6

# REQUIRES: l1 and l2 to be sorted 
# EFFECTS: return sorted linked list
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ans = l1
    while (l1 != None or l2 != None):
        if (l2.val <= l1.val):
            ans.next = ListNode(l2.val)
            l2 = l2.next
        else:
            ans.next = ListNode(l1.val)
            l1 = l1.next
    while (l1 == None and l2 != None):
        ans.next = ListNode(l2.val)
        l2 = l2.next
    while (l2 == None and l1 != None):
        ans.next = ListNode(l1.val)
        l1 = l1.next       

    return ans
        

aa = mergeTwoLists(l1,l2)
print(1)
while (aa != None):
    print(aa.val)
    aa = aa.next
