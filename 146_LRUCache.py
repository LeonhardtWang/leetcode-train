# 哈希表+双向链表
class DLinkedList(object):
    """双向链表"""
    def __init__(self, key=0, value=0):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.head, self.tail = DLinkedList(), DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
    
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key)
        if node:
            node.value = value
            self._move_to_head(node)
        else:
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key] # 记得删除
                self.size -= 1
            new_node = DLinkedList(key, value)
            self._add_node(new_node)
            self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)