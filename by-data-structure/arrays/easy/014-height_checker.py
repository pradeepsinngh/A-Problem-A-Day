# Prob: Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        sortedHeights = sorted(heights)
        counter = 0
        
        for i in range(0,len(heights)):
            
            if sortedHeights[i] != heights[i]:
                counter += 1
        
        return counter
