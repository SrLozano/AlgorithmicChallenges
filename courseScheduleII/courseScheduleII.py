class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        output = []
        visit, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True

            cycle.add(c)
            for pre in preMap[c]:
                if dfs(pre) == False:
                    return False
            cycle.remove(c)

            visit.add(c)
            output.append(c)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output
