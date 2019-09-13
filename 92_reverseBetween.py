# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        record_m = m
        start = head
        r = n - m + 1
        m -= 1
        while m > 0:
            if m == 1:
                first = start
            start = start.next
            m -= 1
                    
        end = start
        while r > 0:
            if r == 1:
                tmp = end.next
                end.next = None
                end = tmp
            else:
                end = end.next
            r -= 1
        h, t = self.reverse(start) # 返回投和位
        if record_m > 1:
            first.next = h
        t.next = end
            
        return head if record_m > 1 else h
        
        
    def reverse(self, head):
        tail = head
        Node = head
    
        remain = head.next
        while remain:
            tmp = remain.next
            remain.next = Node
            Node = remain
            remain = tmp
        return Node, tail
            
            
        
            