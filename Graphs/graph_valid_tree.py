'''
Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.
'''

# Key Ideas:
# Recall that a valid tree is a graph that is connected and does not contain any cycles.
# We can run DFS starting at any arbitrary node. During the DFS, if we encounter a node that 
# has already been visited, it means the graph contains a cycle, so we return False. However, 
# we have to handle the case where we are looking back at the parent node. We can do this by
# passing in the parent node to the DFS function. After DFS finishes, we check if the length 
# of the visited set is equal to the number of nodes n. This tells us if the graph is connected. 


# Runtime: O(V + E) where V is the number of nodes and E is the number of edges. This is because, 
# DFS visits each node and each edge at most once. 


from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for v in adj_list[node]:
                if node == v or (v != parent and not dfs(v, node)):
                    return False
            
            return True


        if dfs(0, -1) and len(visited) == n:
            return True
        return False