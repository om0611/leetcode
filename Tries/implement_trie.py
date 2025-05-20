'''
208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to 
efficiently store and retrieve keys in a dataset of strings. There are various 
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the 
        trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously 
        nserted string word that has the prefix prefix, and false otherwise.
'''


# Key Ideas:
# The Trie class represents the whole tree. To represent each node in the tree,
# we need a Node class. 
# Within the Node class, we need to store its children and a boolean indicating 
# whether the word ending at that node is a valid word.
# To store the children, we can use a dict that maps character to the 
# corresponding node. 
# Insert, search, and startsWith, are all involve traversing down the tree and 
# are very similar. 

class Node:

    def __init__(self):
        self.children = {}
        self.isValid = False

class Trie:

    def __init__(self):                             # O(1)
        self.root = Node()

    def insert(self, word: str) -> None:            # O(len(word))
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]

        node.isValid = True


    def search(self, word: str) -> bool:            # O(len(word))
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.isValid

    def startsWith(self, prefix: str) -> bool:      # O(len(prefix))
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True
