# Prob: Minimum Absolute Difference
'''
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr
'''

# sol1: 

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
        arr.sort()
        res = []
        op = []
        l = len(arr)
        max_num = max(arr)
        min_num = min(arr)
        abs_diff = abs(max_num - min_num)
        
        for i in range(l-1):
            diff = abs(arr[i] - arr[i+1])
            
            if diff < abs_diff:
                abs_diff = diff
                res.append(diff)
        
        min_abs_diff = min(res)
        
        for i in range(l-1):
            diff = abs(arr[i] - arr[i+1])
            
            if diff == min_abs_diff:
                op.append([arr[i], arr[i+1]])
                
        return op
