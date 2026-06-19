# M-Coloring Problem


# Approach:
# For each node, try all m colors if that is safe and backtrack if something break and return False

# Inside issafe check if the node,col is not same as its neighs.
# return true or false accordingly


class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        
        adj = [[] for _ in range(v)]
        
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        color = [-1]*v
        
        def helper(noden):
            if noden == v:
                return True
            
            
            for col in range(m):
                if self.isSafe(noden,col,adj,color):
                    color[noden] = col
                    if helper(noden+1):
                        return True
                    color[noden] = -1
            
            return False
        
        return helper(0)
        
        
    def isSafe(self, node, col, adj, color):
        
        for neigh in adj[node]:
            if color[neigh] != -1 and col == color[neigh]:
                return False
            
        return True
        
        
        