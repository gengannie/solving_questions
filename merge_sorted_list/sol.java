// https://leetcode.com/problems/add-two-numbers/
// QID: 2
// difficulty: medium
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.lang.Math;
class Solution {
    public ListNode addNodes(ListNode l1, ListNode l2, ListNode previous, boolean carry){
        ListNode emp = new ListNode ();
        if (l1 != null && l2 != null){
            int sumOfDigits = l1.val + l2.val;
            if (carry){
                sumOfDigits += 1;
            }
            if (sumOfDigits >= 10){
                carry = true;
                previous.val = sumOfDigits%10;
            } else {
                previous.val = sumOfDigits;
                carry = false;
            }
            l1 = l1.next;
            l2 = l2.next;
            previous.next = addNodes (l1, l2, emp, carry);
        } else if (l1 == null && l2 != null) {
            int sumOfDigits = l2.val;
            if (carry){
                sumOfDigits += 1;
            }
            if (sumOfDigits >= 10){
                carry = true;
                previous.val = sumOfDigits%10;
            } else {
                previous.val = sumOfDigits;
                carry = false;
            }
            l2 = l2.next;
            previous.next = addNodes (l1, l2, emp, carry);
        } else if (l2 == null && l1 != null){
            int sumOfDigits = l1.val;
            if (carry){
                sumOfDigits += 1;
            }
            if (sumOfDigits >= 10){
                carry = true;
                previous.val = sumOfDigits%10;
            } else {
                previous.val = sumOfDigits;
                carry = false;
            }
            l1 = l1.next;
            previous.next = addNodes (l1, l2, emp, carry);
            
        } else if (carry){
            previous.val = 1;
            carry = false;
            previous.next = addNodes (l1, l2, emp, carry);
            
        } else {
            return null;
        }
        return previous;
        
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode emptyNode = new ListNode(); 
        addNodes(l1, l2, emptyNode, false);
        return emptyNode;
        
    }
}
