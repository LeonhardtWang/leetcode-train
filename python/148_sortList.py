# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow_ptr = head
        fast_ptr = head.next.next
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        right_list = slow_ptr.next
        slow_ptr.next = None
        left_list = head
        
        sort_left_list = self.sortList(left_list)
        sort_right_list = self.sortList(right_list)
        
        res = ListNode(0)
        node = res
        while sort_left_list or sort_right_list:
            if sort_left_list and not sort_right_list:
                node.next = sort_left_list
                break
            elif not sort_left_list and sort_right_list:
                node.next = sort_right_list
                break
            else:
                if sort_left_list.val > sort_right_list.val:
                    node.next = sort_right_list
                    sort_right_list = sort_right_list.next
                else:
                    node.next = sort_left_list
                    sort_left_list = sort_left_list.next
                node = node.next
        return res.next
            