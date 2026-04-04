class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for crs, pr in prerequisites:
            prereqs[crs].append(pr)

        visited = set()
        def dfs(curr):
            if curr not in prereqs:
                return True
            if curr in visited:
                return False
            
            visited.add(curr)
            
            for pr in prereqs[curr]:
                if not dfs(pr): return False
            visited.remove(curr)
            prereqs[curr] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
            
        
        
