class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i: [] for i in range(numCourses)}
        for crs, pr in prerequisites:
            prereqs[crs].append(pr)
        
        cycle = set()
        visited = set()
        output = []
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visited:
                return True
            
            cycle.add(curr)
            for pr in prereqs[curr]:
                if not dfs(pr): return False
            cycle.remove(curr)
            visited.add(curr)
            output.append(curr)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return output