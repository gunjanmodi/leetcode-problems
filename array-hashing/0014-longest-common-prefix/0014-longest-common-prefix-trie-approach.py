class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.end_of_word = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            trie.insert(word)

        root = trie.root

        result = []
        while root:
            if len(root.children) > 1 or root.end_of_word:
                break
            key = list(root.children)[0]
            result.append(key)
            root = root.children[key]
        return ''.join(result)


        
        
        

            
        
