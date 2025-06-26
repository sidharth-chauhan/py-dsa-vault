'''
🔢 leetcode 1431. Kids With the Greatest Number of Candies
link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
'''

def kidsWithCandies(self, candies, extraCandies):
        arr=[]
        
        for i in range(0,len(candies)):
            count=0
            for j in candies:
                if j>candies[i]+extraCandies:
                    count+=1
            if count>0:
                arr.append(False)
            else:
                arr.append(True)
        return arr

                

                
        