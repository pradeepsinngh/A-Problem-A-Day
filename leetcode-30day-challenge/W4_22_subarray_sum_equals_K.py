'''
# Prob: Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Input:nums = [1,1,1], k = 2
Output: 2

'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        hashTable = collections.defaultdict(lambda:0)
        running_sum = 0
        
        for n in nums:
            running_sum += n
            sum = running_sum - k
            
            if sum in hashTable:
                count += hashTable[sum]
            if running_sum == k:
                count += 1
            
            hashTable[running_sum] += 1
        return count
