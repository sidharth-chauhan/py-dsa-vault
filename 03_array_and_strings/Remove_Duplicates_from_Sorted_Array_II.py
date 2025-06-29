'''
🔢 leetcode Problem: Remove Duplicates from Sorted Array II
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''

def removeDuplicates(self, nums):
        start =0
        for i in range(2,len(nums)):
            if nums[i]!=nums[start]:
                temp=nums[i]
                nums[i]=nums[start+2]
                nums[start+2]=temp
                start+=1
        return start+2