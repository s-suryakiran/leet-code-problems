class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        cycle = set()
        ans = []
        def dfs(course):
            if course in cycle:
                return False
            if graph[course] == [] :
                if course not in visited:
                    ans.append(course)
                    visited.add(course)
                return True

            cycle.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            graph[course] = []
            if course not in visited:
                ans.append(course)
                visited.add(course)
            return True


        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return ans
        