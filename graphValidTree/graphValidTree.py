class Solution:
    # DFS solution
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # all nodes should be connected with an edge
        if len(edges) > (n - 1):
            return False

        # get a nicer representation of neighbours
        adjacent_nodes = [[] for _ in range(n)]
        for u, v in edges:
            adjacent_nodes[u].append(v)
            adjacent_nodes[v].append(u)

        visit = set()

        def dfs(node, parent):
            # if already visit there is a loop
            if node in visit:
                return False
            
            visit.add(node)
            for neighbour in adjacent_nodes[node]:
                # parent is already checked
                if neighbour == parent:
                    continue
                # recursion
                if not dfs(neighbour, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n