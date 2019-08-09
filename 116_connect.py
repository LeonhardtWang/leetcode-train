"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        root.next = None
        left = self.connect(root.left)
        right = self.connect(root.right)
        left_node = left
        right_node = right
        while left_node:
            left_node.next = right_node
            left_node = left_node.right
            right_node = right_node.left
        root.left = left
        root.right = right
        return root