# Prob: Subdomain visit count

# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format 
# as the input, and in any order), that explicitly counts the number of visits to each subdomain


# Sol1:

# Time Complex = O(N)
# Space Complex = O(N)

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        ans1 = collections.Counter()
        ans2 = []
        
        for domains in cpdomains:
            count, domain = domains.split()
            count = int(count)
            frags = domain.split('.')
            
            for i in range(len(frags)):
                ans1[".".join(frags[i:])] += count
                
        for ct, domain in ans1.items():
            ans2.append("{} {}".format(domain, ct))
        
        return ans2
                
            
        
