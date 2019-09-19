# Prob: Minimum Index Sum of Two Lists

# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented 
# by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between 
# answers, output all of them with no order requirement. You could assume there always exists an answer. 



# Sol1 : Iterate through both list and keep checkiing index sum

# Time Complx: O(m + n), where m and n are len of both list
# Space Complx: O(m + n)


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        l1 = len(list1)
        l2 = len(list2)
        res = []
        prev_sum = l1+ l2
        
        for i in range(l1):
            index_sum = 0
            for j in range(l2):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum <= prev_sum:
                        res.append(list1[i])
                        prev_sum = index_sum
                        
        return res
                    
                
                
