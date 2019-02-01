# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 方法一：将值存入list后，再比较左右的值
    '''
    def yield_head(self, head):
        while head:
            yield head.val
            head = head.next
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head_list = [i for i in self.yield_head(head)]
        
        return head_list == head_list[::-1]
        
        #下面与上一句作用相同
        #while len(head_list) > 1:
        #    if head_list.pop(0) == head_list.pop(-1):
        #        continue
        #    else:
        #        return False
        #return True
    '''
    
    # 方法二：找到利用快慢指针找到中间结点，再比较左部分和翻转后的右部分
    def isPalindrome(self, head):
        # 找中间节点，最终slow_ptr：奇数为(n+1)/2，偶数为n/2
        slow_ptr = fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # 翻转后半部分,赋值到inv
        pre = None
        while slow_ptr:
            temp = slow_ptr.next
            inv = slow_ptr
            inv.next = pre
            pre = inv
            slow_ptr = temp
        
        # 比较
        while head and head.next and inv:
            if inv.val == head.val:
                inv = inv.next
                head = head.next
                continue
            else:
                return False
        return True
            
        