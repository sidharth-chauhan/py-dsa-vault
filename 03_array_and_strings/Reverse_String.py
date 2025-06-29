'''
🔢 leetcode Problem 344: Reverse String
link: https://leetcode.com/problems/reverse-string/
'''

def reverseString(self, s):
        a=0
        b=len(s)-1
        while a<b:
            temp=s[a]
            s[a]=s[b]
            s[b]=temp
            a+=1
            b-=1
        return s