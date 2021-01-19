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
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode node1 = l1;
        ListNode node2 = l2;
        ListNode ansHead = new ListNode((node1.val + node2.val)%10);
        ListNode curr = ansHead;
        int carry = ((node1.val + node2.val)/10);
        
        if(node1.next == null && node2.next == null){ 
            if(carry != 0){
                    curr.next = new ListNode(carry);
            }
            return ansHead;
        }
        while(true){
            int num1;
            int num2;
            int sum;
            
            if(node1.next != null && node2.next != null){
                node1 = node1.next;
                node2 = node2.next;
            }
            else if(node1.next != null && node2.next == null){
                node1 = node1.next;
                node2.next = new ListNode(0);
                node2 = node2.next;
            }
            else if(node1.next == null && node2.next != null){
                node2 = node2.next;
                node1.next = new ListNode(0);
                node1 = node1.next;
            }
            else if(node1.next == null && node2.next == null){           
                if(carry != 0){
                    curr.next = new ListNode(carry);
                    break;
                }
                break;
            }
            
            num1 = node1.val;
            num2 = node2.val;
            
            sum = num1 + num2 + carry;
            carry = sum/10;
            
            curr.next = new ListNode(sum%10);
            curr = curr.next;
            
        }
        return ansHead;
    }
}