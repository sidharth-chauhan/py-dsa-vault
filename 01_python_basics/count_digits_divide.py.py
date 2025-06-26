class Solution(object):
    def countDigits(self, num):
        count=0
        original =num
        while num>0:
            div=num%10
            if original%div==0:
                count+=1
            num=num//10
        return count
        