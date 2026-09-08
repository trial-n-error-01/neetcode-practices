# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
           
        curNode = head
        prev = None

        while curNode:
            nextNode = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nextNode
        
        return prev