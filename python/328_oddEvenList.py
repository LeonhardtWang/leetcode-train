# 单链表实现
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def LinkList(input):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next
    res = dummyRoot.next
    return res

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        node_odd = head
        node_even_head = head.next
        node_even = head.next
        while True:
            if node_even.next is not None:
                node_odd.next = node_even.next
                node_odd = node_odd.next
            else:
                return head
            if node_odd.next is not None:
                node_even.next = node_odd.next
                node_even = node_even.next
                node_odd.next = node_even_head
            else:
                node_odd.next = node_even_head
                node_even.next = None
                return head

test = LinkList([2,1,3,5,6,4,7])
test = Solution().oddEvenList(test)
while test:
    print(test.val, end=',')
    test = test.next
            
