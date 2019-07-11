# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.node = ListNode(0)
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        else:
            val = l1.val + l2.val
            carry = val // 10
            mod = val % 10
            
            res = ListNode(mod)
            l1 = l1.next
            l2 = l2.next
            self.addTwoNumbersCore(res, l1, l2, carry)
            return res
            
    def addTwoNumbersCore(self, res, l1, l2, carry):
        if l1 is None and l2 is None:
            if carry > 0:
                res.next = ListNode(carry)
            else:
                res.next = None
        else:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            val = l1_val + l2_val + carry
            carry = val // 10
            mod = val % 10
            
            res.next = ListNode(mod)
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            self.addTwoNumbersCore(res.next, l1, l2, carry)
        
            