'''
🔢 leetcode 231: Power of Two
link: https://leetcode.com/problems/power-of-two/
'''
def isPowerOfTwo(self, n):
        if n<1:
            return False
        while n%2==0:
            n=n//2
        return n==1