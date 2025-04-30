'''
133. Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
'''

# Key Ideas:
# Run DFS on the given node. During each DFS call, create a new node for the current node and 
# add the mapping between the old node and the new node to a hash map. 
# Then, iterate over all the neighbors, calling dfs on the neighbor if it has not already 
# been explored, and then adding it to the neighbors list for the current node.

# Runtime: O(V + E) because each node and edge is visited at most once by DFS. If the graph is sparse
# the runtime becomes O(V), and if the graph is dense, the runtime becomes O(E). 


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}

        def dfs(v):
            new = Node(val=v.val)
            nodes[v] = new

            for u in v.neighbors:
                if u not in nodes:
                    dfs(u)
                new.neighbors.append(nodes[u])
            
        dfs(node)
        return nodes[node]