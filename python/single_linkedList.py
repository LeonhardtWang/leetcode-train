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

# 链表赋值为引用，但注意以下情形，c不受d改变影响
a = LinkList([1,3,4,5,6])
b = a.next
c = a
c.next = None # 若改成d.next.next = None？
b.next.next = LinkList([8,9])
