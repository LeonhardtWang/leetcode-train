# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        ptr_slow = head
        ptr_fast = head.next
        while ptr_fast:
            if ptr_fast.val == val:
                ptr_slow.next = ptr_fast.next
                ptr_fast = ptr_fast.next
            else:
                ptr_slow = ptr_slow.next
                ptr_fast = ptr_fast.next
        if head.val == val:
            head = head.next
        return head
                