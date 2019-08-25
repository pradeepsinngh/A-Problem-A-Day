# Prob: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(0, n):
            nums1[m+i] = nums2[i]
        
        nums1.sort()

