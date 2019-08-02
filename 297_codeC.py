# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        s = ''
        while queue:
            node = queue.popleft()
            if node:
                s += str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)
            else:
                s += 'None' + ','
        return '[' + s[:-1] + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_split = data[1:-1].split(',')
        r = data_split[0]
        if r == 'None':
            return None
        root = TreeNode(r)
        queue_1 = deque([root])
        queue_2 = deque(data_split[1:])
        while queue_1 and queue_2:
            node = queue_1.popleft()
            left = queue_2.popleft()
            right = queue_2.popleft()
            left = TreeNode(int(left)) if left != 'None' else None
            right = TreeNode(int(right)) if right != 'None' else None
            
            node.left = left
            node.right = right
            
            if node.left:
                queue_1.append(node.left)
            if node.right:
                queue_1.append(node.right)
        return root


test = '[1,2,3,None,None,4,5]'
codec = Codec()
root = codec.deserialize(test)
root_s = codec.serialize(root)