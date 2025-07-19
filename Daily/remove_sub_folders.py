'''
1233. Remove Sub-Folders from the Filesystem

Given a list of folders folder, return the folders after removing all 
sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder 
of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". 
For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of 
"/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' 
followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an 
empty string and "/" are not.
'''


# Key Ideas:
# This is a prefix matching problem, so we can use a Prefix Tree, also called a
# Trie. We will only add folders that are not sub-folders to our trie. To do
# this, we should first sort the folders by their length. This is to ensure 
# that each sub-folder comes after its parent folder as we iterate through them.
# For each folder path, we split it by "/" and go down the trie based on the 
# folder names. If on our way down a path in the trie, we reach a node that has 
# end_of_path = True, we know that our current folder is a sub-folder, so we 
# don't add it to our result list. If the path does not exist in the trie, we
# add it to the trie and add the path to the result list.


# Runtime: O(n * l) where n is the length of the input list and l is the length 
# of each folder path. Sorting the input list takes O(n log n). Iterating 
# through each folder in the input list and searching for it in the trie is 
# O(n * l). 

# Space: O(n * l) because in the worst case, each path in the trie is 
# completely unique. Since there are n folder paths and each folder path can be
# length l.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_path = False

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort(key=lambda x: len(x))
        root = TrieNode()
        res = []
        for path in folder:
            folders = path.split("/")
            curr = root
            exists = False
            for i in range(1, len(folders)):
                f = folders[i]
                if f not in curr.children:
                    curr.children[f] = TrieNode()

                elif curr.children[f].end_of_path:
                    exists = True

                curr = curr.children[f]

                if exists:
                    break

            curr.end_of_path = True
            if not exists:
                res.append(path)

        return res