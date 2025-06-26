def isPalindrome(self, x):
        original =x
        count=0
        while x>0:
            div=x%10
            count=count*10+div
            x=x//10
        if original==count:
            return True
        else:
            return False
print(isPalindrome(0, 121))