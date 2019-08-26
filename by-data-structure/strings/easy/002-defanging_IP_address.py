# Prob: Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# Sol1: 
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
       
        return address.replace('.', '[.]')
    
 # Sol2:
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        return ('[.]'.join(address.split('.')))
