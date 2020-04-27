'''
# Prob: Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.


'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        res = []
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
            
        for i in range(numCourses):
            if not self.dfs(graph, visited, res, i):
                return []
        
        return res
    
    def dfs(self, graph, visited, res, i):
        
        # if already visited
        if visited[i] == -1:
            return False
        
        # if being visited
        if visited[i] == 1:
            return True
        
        # mark being visited
        visited[i] = -1
        
        # visit all neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, res, j):
                return res
        
        visited[i] = 1
        res.append(i)
        return res
            
