class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)
        
        queue = deque()
        finish = 0

        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)
                finish += 1
        
        while queue:
            prereq = queue.popleft()
            for course in adj[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
                    finish += 1
        
        return finish == numCourses