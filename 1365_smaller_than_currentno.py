'''
🔢 leetcode 1365: How Many Numbers Are Smaller Than the Current Number
link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
'''
def smallerNumbersThanCurrent(self, nums):
    arr=[]
    for i in nums:
        count =0
        for j in nums:
            if i >j:
                count+=1
        arr.append(count)
                    
    return arr 