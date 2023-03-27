class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # if not node:
        #     return None
        # visited = {}
        # def dfs(node):
        #     if node in visited:
        #         return visited[node]
        #     clone = Node(node.val)
        #     visited[node] = clone
        #     for n in node.neighbors:
        #         clone.neighbors.append(dfs(n))
        #     return clone
        # return dfs(node)
        curNode = node
        if not curNode:
            return None
        visited = {}
        val, neighbors = curNode.val, curNode.neighbors
        clone = Node(val)
        clone.neighbors = neighbors
        visited[clone] = clone.neighbors
        while neighbors:
            curNode = neighbors.pop()
            if curNode not in visited:
                val, neighbors = curNode.val, curNode.neighbors
                clone = Node(val)
                clone.neighbors = neighbors
                visited[clone] = clone.neighbors
        
        return visited


            