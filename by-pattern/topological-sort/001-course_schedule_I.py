'''
# Prob: Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
'''



class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        
        # visit all nodes
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        
        # if already visited
        if visited[i] == -1:
            return False
        
        if visited[i] == 1:
            return True
        
        # mark as being visited 
        visited[i] = -1
        
        # visit all neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited,j):
                return False
        # mark as done visited
        visited[i] = 1
        
        return True
