# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
            
        slow_ptr = head
        fast_ptr = head.next.next
        
        # 找到快慢指针相遇的节点
        while fast_ptr != slow_ptr:
            slow_ptr = slow_ptr.next
            if not fast_ptr or not fast_ptr.next:
                return None
            else:
                fast_ptr = fast_ptr.next.next
        
        # 计算到下次相遇所需要的步数，即为环形部分的节点数目
        cycle_len = 0
        while fast_ptr != slow_ptr or cycle_len == 0:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            cycle_len += 1
        
        fast_ptr = head
        slow_ptr = head
        while cycle_len:
            fast_ptr = fast_ptr.next
            cycle_len -= 1
            
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            
        return slow_ptr