'''
212. Word Search II

Given an m x n board of characters and a list of strings words, return all 
words on the board.

Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same 
letter cell may not be used more than once in a word.
'''


# Key Ideas:
# Use a trie to store the words so that we can check prefixes efficiently.
# At each cell in the board, run DFS and check prefixes with the trie. 

class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        root = Node()

        # Initialize a trie with all the words.
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.endOfWord = True
        
        foundWords = set()
        res = []
        visit = set()

        def dfs(i, j, currNode, currWord):
            if (i < 0 or i >= m or j < 0 or j >= n
                or ((i, j) in visit) or (board[i][j] not in currNode.children)):
                return

            visit.add((i, j))
            newNode = currNode.children[board[i][j]]
            currWord += board[i][j]
            if newNode.endOfWord and currWord not in foundWords:
                res.append(currWord)
                foundWords.add(currWord)
            
            if not newNode.children:
                visit.remove((i, j))
                return

            dfs(i-1, j, newNode, currWord)
            dfs(i+1, j, newNode, currWord)
            dfs(i, j-1, newNode, currWord)
            dfs(i, j+1, newNode, currWord)

            visit.remove((i, j))


        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return res