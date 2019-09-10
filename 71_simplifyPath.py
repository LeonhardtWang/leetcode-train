# 方法一：链表（效率低）
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None

class Solution:
    def simplifyPath(self, path: str) -> str:
        head = Node('')
        ptr = head
        while path:
            nex, path = self.get_next(path)
            # print(nex)
            if not nex:
                break
            if nex == '.':
                continue
            elif nex == '..':
                if ptr.val:
                    ptr = ptr.pre
            else:
                if ptr.next is None or ptr.next.val != nex:
                    ptr.next = Node(nex)
                    pre = ptr
                    ptr = ptr.next
                    ptr.pre = pre
                else:
                    ptr = ptr.next
        res = ''
        if head.val == ptr.val == '':
            return '/'
        else:
            head = head.next
            while head != ptr:
                res += '/' + head.val
                head = head.next
            return res + '/' + head.val
                 
    def get_next(self, path):
        for i, s in enumerate(path):
            if s != '/':
                break
        if s == '/':
            i += 1
        j = i + 1
        for j in range(i+1, len(path)):
            if path[j] == '/':
                break
        if j < len(path) and path[j] != '/':
            j += 1
        return path[i:j], path[j:]
        
# 方法二：栈
class Solution2:
    def simplifyPath(self, path: str) -> str:
        path_lis = path.split('/')
        stack = []
        for item in path_lis:
            if item == '..':
                if stack:
                    stack.pop()
            elif item and item != '.':
                stack.append(item)
        return '/'+'/'.join(stack)