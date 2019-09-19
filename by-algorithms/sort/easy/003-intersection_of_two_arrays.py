# Prob: Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.
# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Sol1 : Using dict()
# ----------------------------

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dic = {}
        res = []
        
        for num in nums1:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] -= 1
                
        return res
        
  
# Sol 2: Using Two pointers
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        num1, num2 = sorted(nums1), sorted(nums2)
        pt1, pt2 = 0, 0
        res = []
        
        while True:
            try:
                if num1[pt1] > num2[pt2]:
                    pt2 += 1
                elif num2[pt2] > num1[pt1]:
                    pt1 += 1
                else:
                    res.append(num1[pt1])
                    pt1 += 1
                    pt2 += 1
                    
            except IndexError:
                break
                
        return res
                    
