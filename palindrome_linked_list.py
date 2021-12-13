# given the head of a singly linked list, return True if palindrome

#approach 2: HARD!
# O(n) time, but O(1) space
# get the middle node of linked list
# reverse second half,
# compare the values 
# note this does it in-place (doesn't allocate extra memory)

from typing import no_type_check_decorator


def get_middle_node(node):
    slow = node
    fast = node
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
def reverse_ll(node):
    prev = None
    curr = node
    while curr:
        catch = curr.next
        curr.next = prev
        prev = curr
        curr = catch
    return prev
def is_palindrome_optimized(head):
    if not head:
        return False
    first_half_end = get_middle_node(head)
    second_half_start = reverse_ll(first_half_end.next)
    first, second = head, second_half_start
    res = True
    while first and second:
        if first.val != second.val:
            res = False
            break
        first = first.next
        second = second.next
    first_half_end.next = reverse_ll(second_half_start) # restore linked list
    return res


# approach 1
# n is the number of elements in linked list
# O(n) time and space
# traverse through linked list, storing every element in list, then 2 pointers
def is_palindrome(head): # method sig: head : Optional [ListNode] -> bool
    if not head:
        return False
    arr = []
    tmp = head
    while tmp:
        arr.append(tmp.val)
        tmp = tmp.next
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

