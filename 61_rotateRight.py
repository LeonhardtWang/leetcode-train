# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        k %= length
        k = length - k
        first = head
        while k > 1:
            first = first.next
            k -= 1 
        res = first.next
        ptr = first.next
        first.next = None
        if res is None:
            return head
        while ptr.next:
            ptr = ptr.next
        ptr.next = head
        return res
            
            