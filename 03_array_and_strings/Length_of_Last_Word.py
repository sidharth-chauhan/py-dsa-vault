'''
🔢 leetcode Problem 58: Length of Last Word
link: https://leetcode.com/problems/length-of-last-word/

'''
def lengthOfLastWord(self, s):
        s=s.strip()
        if s.count(" ")==0:

            return len(s)
        for i in range(len(s)-1,0,-1):
            if s[i]==" ":
                return len(s)-i-1