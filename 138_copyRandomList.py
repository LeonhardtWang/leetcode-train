# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# 方法一：先去除random，再根据记录的random指向的位置，加入random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        pHead = head
        node = self.remove_random_copy(pHead) # 去除random指针返回拷贝
        cycle_dic = {} # hash表记录每个节点random指向的位置, 从0开始，-1表示None
        index = 0
        while pHead: # 记录每个节点random指向的节点
            random_node = pHead.random
            if random_node: 
                cyc_index = 0
                tmp = head
                while tmp != random_node:
                    cyc_index += 1
                    tmp = tmp.next
            else:
                cyc_index = -1
            cycle_dic[index] = cyc_index
            pHead = pHead.next
            index += 1
            
        # 加入random指针
        pNode = node
        i = 0
        while pNode:
            ran_i = cycle_dic[i]
            if ran_i >= 0:
                tmp = node
                while ran_i:
                    tmp = tmp.next
                    ran_i -= 1
                pNode.random = tmp
            pNode = pNode.next
            i += 1
        return node
                 
    def remove_random_copy(self, head):
        pHead = head
        node = Node(pHead.val, None, None)
        pNode = node
        while pHead.next:
            pHead = pHead.next
            pNode.next = Node(pHead.val, None, None)
            pNode = pNode.next
        return node


# 方法二：回溯
class Solution2(object):
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node
        next_node = self.copyRandomList(head.next)
        random_node = self.copyRandomList(head.random)
        node.next = next_node
        node.random = random_node
        return node

# 方法三：O(N)空间的迭代
class Solution3(object):
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        head_q = head
        node = Node(head.val, None, None)
        self.visited[head_q] = node
        while head_q:
            random_node = self._get_clone_node(head_q.random)
            next_node = self._get_clone_node(head_q.next)
            node.random = random_node
            node.next = next_node
            head_q = head_q.next
            node = node.next
        return self.visited[head]
            
    def _get_clone_node(self, head):
        if head:
            if head in self.visited:
                return self.visited[head]
            else:
                node = Node(head.val, None, None)
                self.visited[head] = node
                return self.visited[head]
        else:
            return None

# 方法四：O(1)空间的迭代
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        ptr = head
        while ptr:
            node = Node(ptr.val, None, None)
            node.next = ptr.next
            ptr.next = node
            ptr = ptr.next.next
        
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        res = head.next
        old_node = head
        new_node = head.next
        while old_node:
            old_node.next = old_node.next.next
            new_node.next = new_node.next.next if new_node.next else None
            old_node = old_node.next
            new_node = new_node.next
        return res
        
        
