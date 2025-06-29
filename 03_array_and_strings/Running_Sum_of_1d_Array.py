'''
🔢 leetcode Problem 1480: Running Sum of 1d Array
link: https://leetcode.com/problems/running-sum-of-1d-array/
'''


def runningSum(self, nums):
        count =[]

        count.append(nums[0])
        if len(nums)>1:
            for i in range(1,len(nums)):
                k=nums[i]+count[i-1]
                count.append(k)
        return count
