# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(0)
        node = res
        while head:
            if head.next is None:
                node.next = head
                return res.next
            node.next = head.next
            node = node.next
            tmp = node.next
            node.next = head
            node = node.next
            head = tmp
        node.next = None
        return res.next