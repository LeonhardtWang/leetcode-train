# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length < k:
            return head
        sum_length = 0
        final_res = None
        node = head
        while node and length - sum_length >= k:
            cur = node
            record = k
            while record > 1:
                node = node.next
                record -= 1
            tmp = node.next
            node.next = None
            node = tmp
            cur_head, cur_tail = self.helper(cur)
            if not final_res:
                final_res = cur_head
                final_res_tail = cur_tail
            else:
                final_res_tail.next = cur_head
                final_res_tail = cur_tail
            sum_length += k
        final_res_tail.next = node
        return final_res
                  
    def helper(self, node):
        if not node.next:
            return node, node
        remain = node.next.next
        res = node.next
        res.next = node
        node.next = None
        while remain:
            tmp = remain.next
            remain.next = res
            res = remain
            remain = tmp
        return res, node
        