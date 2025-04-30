class Node:
    def __init__(self,val=0, neighbors=None):
        self.val=val
        self.neighbors=neighbors

class CloneGraph:
    def cloneGraph(self, node):
        if not node:
            return None
        visited={}
        def clone(node):
            if node in visited:
                return visited[node]
            
            copy=Node(node.val)
            visited[node]=copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy
        return clone(node)
