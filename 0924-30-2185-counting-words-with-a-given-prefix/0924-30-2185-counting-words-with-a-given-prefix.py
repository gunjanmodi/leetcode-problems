class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_trie = Trie()
        for word in words:
            prefix_trie.insert(word)
        return prefix_trie.search(pref).count


class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        parent = self.root
        for c in word:
            if c not in parent.children:
                parent.children[c] = TrieNode()
            parent = parent.children[c]
            parent.count += 1
        parent.eow = True

    def search(self, prefix) -> dict:
        parent = self.root
        for c in prefix:
            if c in parent.children:
                parent = parent.children[c]
            else:
                return TrieNode()
        return parent
