# Prob: Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Sol 1:
# ---------------------------------
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sortedNums = sorted(nums)
        return sortedNums[-k]
        
        
