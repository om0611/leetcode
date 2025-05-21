'''
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string 
matches any previously added string.

Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched 
        later.
    - bool search(word) Returns true if there is any string in the data 
        structure that matches word or false otherwise. word may contain dots 
        '.' where dots can be matched with any letter.
'''

# Key Ideas:
# We can use a trie to efficiently solve this problem.
# Add() is trivial.
# For Search(), create a recursive helper that takes the current node and
# the current index i in word. If word[i] is '.', we iterate over each char
# in the current node's children dict and traverse down each path to search for
# the word. If word[i] is a char, we check if it exists in the current node's
# children dict, and if so, we recruse on that node with index i+1. 


class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):         # O(1)
        self.root = Node()

    def addWord(self, word: str) -> None:       # O(len(word))
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word: str) -> bool:        # O(26^2 * len(word))

        def helper(curr, i):
            if i == len(word) - 1:
                if word[i] == '.':
                    return any(curr.children[c].endOfWord 
                               for c in curr.children)
                else:
                    return (word[i] in curr.children 
                            and curr.children[word[i]].endOfWord)

            if word[i] == '.':
                for c in curr.children:
                    if helper(curr.children[c], i+1):
                        return True
                return False

            return (word[i] in curr.children 
                    and helper(curr.children[word[i]], i+1))
    
        return helper(self.root, 0)
