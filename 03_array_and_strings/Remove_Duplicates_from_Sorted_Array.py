'''
🔢 leetcode 26 - Remove Duplicates from Sorted Array
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

def removeDuplicates(self, nums):
        start =0
        for i in range(1,len(nums)):
            if nums[i]!=nums[start]:
                temp=nums[i]
                nums[i]=nums[start+1]
                nums[start+1]=temp
                start=start+1
            
        return start+1
        