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

sort_linkList = LinkList([1, 1, 2, 3, 3]) # 构造有序单列表

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return head
        ptf = head
        pts = head.next
        while pts:
            if ptf.val == pts.val:
                pts = pts.next
                if not pts:
                    ptf.next = None
                    return head
            else:
                ptf.next = pts
                ptf = ptf.next
                pts = pts.next
        return head
