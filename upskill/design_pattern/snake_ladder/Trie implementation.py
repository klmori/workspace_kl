class TrieNode:
    def __init__(self):
        self.children = {}  # key: char, value: TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        print()
        node.is_end_of_word = True

    # Search a full word in the trie
    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    # Check if any word starts with given prefix
    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    # Helper: traverse the trie to find node matching last char of prefix
    def _find_node(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))     # ✅ True
print(trie.search("app"))       # ✅ True
print(trie.search("appl"))      # ❌ False
print(trie.starts_with("appl"))  # ✅ True
print(trie.starts_with("bat"))  # ❌ False
