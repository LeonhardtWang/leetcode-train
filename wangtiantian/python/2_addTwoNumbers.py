# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        base = l1.val + l2.val
        count = base // 10
        remain = base % 10
        curr_node = ListNode(remain)
        res = curr_node
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            base = l1.val + l2.val + count
            count = base // 10
            remain = base % 10
            curr_node.next = ListNode(remain)
            curr_node = curr_node.next
        rl = l1.next or l2.next
        while rl:
            base = rl.val + count
            count = base // 10
            remain = base % 10
            curr_node.next = ListNode(remain)
            curr_node = curr_node.next
            rl = rl.next
        if count > 0:
            curr_node.next = ListNode(count)
        return res
            
