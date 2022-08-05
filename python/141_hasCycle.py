# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
    
        slow_ptr = head
        fast_ptr = head.next
        while fast_ptr:
            fast_ptr = fast_ptr.next
            if fast_ptr:
                if slow_ptr.val == fast_ptr.val:
                    return True
                else:
                    fast_ptr = fast_ptr.next
                    slow_ptr = slow_ptr.next
        return False
        