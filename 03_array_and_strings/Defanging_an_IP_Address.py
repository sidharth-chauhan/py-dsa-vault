'''
# LeetCode Problem 1108: Defanging an IP Address
link: https://leetcode.com/problems/defanging-an-ip-address/


'''

def defangIPaddr(self, address):
        a=""
        for i in range(0,len(address)):
            if address[i]==".":
                a=a+"[.]"
            else:
               a=a+address[i]

        return a