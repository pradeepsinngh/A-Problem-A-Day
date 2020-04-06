```
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

NOTE:
- All inputs will be in lowercase.
- The order of your output does not matter.

```

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hashmap = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in hashmap:
                hashmap[key] = [s]
            else:
                hashmap[key] += [s]
        return hashmap.values()
