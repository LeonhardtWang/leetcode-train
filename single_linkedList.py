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

LinkList([1,3,4,5,6])