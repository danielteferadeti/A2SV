# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        memo = head
        while memo:
            stack.append(memo)
            memo = memo.next  
            
        while head:
            cur = head
            temp = cur.next
            if temp == None or temp.next == None:
                break
            lastElem = stack.pop()
            prev = stack.pop()
            prev.next = None
            stack.append(prev)
            head.next = lastElem
            lastElem.next = temp
            head = temp 