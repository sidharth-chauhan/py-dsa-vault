'''
🔢 leetcode Problem 151: Reverse Words in a String
link: https://leetcode.com/problems/reverse-words-in-a-string/
'''


def reverseWords(self, s):
        s=s.strip()
        s=s.split()
        s.reverse()
        
        a=""
        
        for i in s:
            a=a+i
            a=a+" "
        a=a.strip()
            
        return a 