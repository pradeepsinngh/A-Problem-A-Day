class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
    # Sol 3:  O(n)
    
        C = collections.Counter(arr)
        count = 0
        for x in C:
            if x+1 in C:
                count += C[x]
    
        return count
        
    # Sol 2: O(n) solution
    
    #    count = 0
    #    array = lambda x:x+1
    #    for val in arr:
    #        if array(val) in arr:
    #            count += 1
    #    return count
    
    # Sol 1: O(n * n) solution
    
    #    arr.sort()
    #    n = len(arr)
    #    curr = 0
    #    nxt = 1
    #    ans = []
        
    #    while curr < n-1:
    #        while nxt < n:
    #            if arr[nxt] == arr[curr] + 1:
    #                ans.append(arr[nxt])
    #                break
    #            nxt += 1
    #        curr += 1
    #        nxt = curr + 1
    #    return len(ans)
    
    
        
            
