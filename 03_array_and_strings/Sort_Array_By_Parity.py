'''
🔢 leetcode 905: Sort Array By Parity
link: https://leetcode.com/problems/sort-array-by-parity/
'''

def sortArrayByParity(self, nums):
        count=0
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                temp=nums[i]
                nums[i]=nums[count]
                nums[count]=temp
                count+=1
        return nums