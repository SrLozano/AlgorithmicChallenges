class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if preMap[c] == []:
                return True
            
            visited.add(c)

            for pre in preMap[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            preMap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): 
                return False
        return True
