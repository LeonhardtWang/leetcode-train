class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tmp = self.tree
        for s in word:
            if s not in tmp:
                tmp[s] = {}
            tmp = tmp[s]
        tmp["end"] = True
                
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tmp = self.tree
        for s in word:
            if s in tmp:
                tmp = tmp[s]
            else:
                return False
        if "end" in tmp:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp = self.tree
        for s in prefix:
            if s in tmp:
                tmp = tmp[s]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert('app')
obj.insert('apple')
obj.insert('beer')
obj.insert('add')
obj.insert('jam')
obj.insert('rental')