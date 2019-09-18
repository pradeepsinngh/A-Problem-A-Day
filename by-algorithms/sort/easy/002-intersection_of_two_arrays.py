# Prob: Intersection of two arrays
# Given two arrays, write a function to compute their intersection.

# Sol1 : Iterate over arr1 and check if that element is present in second array or not.

# Time Complx: O(m + n) where m, n are arr1, arr2 len.
# Space Compx: O(m + n)

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for j in nums1:
            if j in nums2:
                if j not in ans:
                    ans.append(j)
                
        return ans
                
            
# Sol2 : Use two sets

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        arr1 = set(nums1)
        arr2 = set(nums2)
        
        output = []
        
        if len(arr1) < len(arr2):
            for i in arr1:
                if i in arr2:
                    output.append(i)
        else:
            for i in arr2:
                if i in arr1:
                    output.append(i)
                    
        return output
            
                
                
            
