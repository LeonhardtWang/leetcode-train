"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(node):
            if node is None:
                return None

            left = helper(node.left)
            right = helper(node.right)

            if left is None or right is None:
                return node

            left_list = [left]
            right_list = [right]
            while left_list and right_list:
                left_list[-1].next = right_list[0]

                temp_left_list = []
                for left_node in left_list:
                    if left_node.left is not None:
                        temp_left_list.append(left_node.left)
                    if left_node.right is not None:
                        temp_left_list.append(left_node.right)
                temp_right_list = []
                for right_node in right_list:
                    if right_node.left is not None:
                        temp_right_list.append(right_node.left)
                    if right_node.right is not None:
                        temp_right_list.append(right_node.right)
                left_list = temp_left_list
                right_list = temp_right_list
            return node
            
        return helper(root)