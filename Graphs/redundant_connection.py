'''
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no 
cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, 
with one additional edge added. The added edge has two different vertices 
chosen from 1 to n, and was not an edge that already existed. The graph is 
represented as an array edges of length n where edges[i] = [ai, bi] indicates 
that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n 
nodes. If there are multiple answers, return the answer that occurs last in the 
input.
'''


# Key Ideas:
# We can use Disjoint Set / Union Find to tell us if an edge connects two 
# different components. As soon as we encounter an edge that connects two nodes
# that are part of the same connected component (same representative), we 
# return that edge.
# Notice that the number of nodes n is not given. However, we know that we
# started off with a tree and added exactly one more edge. A tree has n - 1
# edges, so the input graph will have exactly n edges. Therefore, 
# n == len(edges).

# Runtime: O(V + E). Initializing the rep and rank arrays take O(V), and 
# iterating over all the edges take O(E). The disjoint set operations have
# an amortized running time of O(1). 


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # A tree has n - 1 edges, and we added one extra edge, 
        # so the graph has n edges.
        n = len(edges)

        rep = [i for i in range(n + 1)]
        rank = [1] * (n+1)

        # Recursive implementation of find set.
        def find(u):
            if u != rep[u]:
                rep[u] = find(rep[u])
            return rep[u]
        
        def union(u, v):
            r1, r2 = find(u), find(v)
            if r1 == r2:
                return 0
            if rank[r1] >= rank[r2]:
                rep[r2] = r1
                rank[r1] += rank[r2]
            else:
                rep[r1] = r2
                rank[r2] += rank[r1]
            return 1

        for u, v in edges:
            if not union(u, v):
                return [u, v]