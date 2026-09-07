class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        res = []

        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)
        
        firstCourses = []
        for course in range(len(indegree)):
            if indegree[course] == 0:
                firstCourses.append(course)
        
        queue = deque()
        finish = 0

        while firstCourses:
            firstCourse = firstCourses.pop()
            queue.append(firstCourse)
            res.append(firstCourse)
            finish += 1
            while queue:
                prereq = queue.popleft()
                for course in adj[prereq]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        queue.append(course)
                        res.append(course)
                        finish += 1
        
        return res if finish == numCourses else []