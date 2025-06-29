'''
🔢 leetcode 125: Valid Palindrome
link: https://leetcode.com/problems/valid-palindrome/
'''

def isPalindrome(self, s):
        s=s.lower()
        a=""

        for i in range(0,len(s)):
            if 96<ord(s[i])<123 or 47<ord(s[i])<58:
                a=a+s[i]
        if a == a[::-1]:
            return True
        else:
            return False
            