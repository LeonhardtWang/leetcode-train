# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        Node = ListNode(None)
        Node.next = head
        ptr1 = Node
        ptr2 = Node.next
        while ptr1:
            while True:
                is_del = False
                while ptr2 and ptr2.next and ptr2.val == ptr2.next.val:
                    is_del = True
                    ptr2 = ptr2.next
                if is_del:
                    ptr2 = ptr2.next
                if not ptr2 or not ptr2.next or (ptr2 and ptr2.next and ptr2.val != ptr2.next.val):
                    break
                
            ptr1.next = ptr2
            ptr2 = ptr2 if ptr2 is None else ptr2.next
            ptr1 = ptr1.next
        return Node.next
            
            