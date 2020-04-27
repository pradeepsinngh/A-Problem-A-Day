'''
Course Schedule III

There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3

'''

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda c:c[1])
        time = ans = 0
        maxDuration = []
        
        for length, deadline in courses:
            if time + length <= deadline:
                time += length
                ans += 1
                heapq.heappush(maxDuration, -length)
            elif maxDuration and length < -maxDuration[0]:
                time += length + heapq.heappushpop(maxDuration, -length)
        return ans
