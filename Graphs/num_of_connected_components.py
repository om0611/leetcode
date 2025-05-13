'''
Number of Connected Components in an Undirected Graph

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] 
means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.
'''

# Solution 1 (DFS)
# Iterate over each node from 0 to n-1, and if the node has not been visited, call DFS on that node
# and mark all nodes connected to it as visited. This will explore one connected component. The number 
# of times you have to run DFS on a new node tells you the number of connected components in the graph.

# Runtime: O(E + V) where E is the number of edges and V is the number of nodes (n). This is because
# DFS visits each node and each edge at most once.

from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for v in adj[node]:
                if v not in visited:
                    dfs(v)
            
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res
    
# Solution 2 (Union Find - Disjoint Set)
# Initialize an array called rep such that for each node u, rep[u] will be the representative of the set containing u. 
# Initially, the rep of each node will be itself. Initialize another array called rank that will store the rank for 
# each node. Rank of a node u is the number of elements in the set whose representative is u. Now, implement two functions:
# find(u) and union(u, v). find(u) finds the representative of u. union(u, v) combines the sets containing u and v if they 
# are disjoint. Now, iterate over each edge and perform the union operation on the two nodes. If the union was successful, 
# we decreased the number of connected components by 1. Initally there would be n connected components since we haven't
# considered any edges. Return the number of connected components after iterating over all the edges.

# Runtime: O(V + E). Initializing the two arrays at the start takes O(V) each. We iterate over every edge, which is 
# O(E). The find and union operations are constant in terms of amortized analysis. 

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        rep = [i for i in range(n)]
        rank = [1] * n

        def find(u):
            res = u

            while res != rep[res]:
                rep[res] = rep[rep[res]]       # path compression
                res = rep[res]
            
            return res

        def union(u, v):
            p1, p2 = find(u), find(v)

            if p1 == p2:
                return 0
            
            if rank[p1] >= rank[p2]:
                rep[p2] = p1
                rank[p1] += rank[p2]
            else:
                rep[p1] = p2
                rank[p2] += rank[p1]
            return 1

        connected = n
        for u, v in edges:
            connected -= union(u, v)
        return connected