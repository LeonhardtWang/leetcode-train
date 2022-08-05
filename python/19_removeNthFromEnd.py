# Definition for singly-linked list.
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

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 找到要删除的节点的前一个节点
        head_quick = head.next
        while head_quick is not None and n > 0:
            head_quick = head_quick.next
            n -= 1
        if n > 1:
            return head
        
        if n == 1:
            return head.next
        
        head_slow = head
        while head_quick is not None:
            head_slow = head_slow.next
            head_quick = head_quick.next
        
        head_slow.next = head_slow.next.next
        
        return head


if __name__ == "__main__":
    head = LinkList([1,2,3,4,5])
    Solution().removeNthFromEnd(head, 2)
          