# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归，耗时800ms，较长
        #if (not head) or (not head.next):
        #    return head
        #elif not head.next.next:
        #    res = head.next
        #    head.next = None
        #    res.next = head
        #    return res
        #else:
        #    res = self.reverseList(head.next)
        #    res_ptr = res
        #    while res_ptr.next:
        #        res_ptr = res_ptr.next
        #    head.next = None
        #    res_ptr.next = head
        #    return res
            
        # 迭代，耗时32ms，beats96.14%
        val_list = []
        head_copy = head
        while head_copy:
            val_list.append(head_copy.val)
            head_copy = head_copy.next
        val_list_rev = val_list[::-1]
        if val_list_rev:
            head_copy = head
            for val in val_list_rev:
                head_copy.val = val
                head_copy = head_copy.next
            head_copy = None
        return head