'''
# LeetCode Problem 121: Best Time to Buy and Sell Stock
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

def maxProfit(self, prices):
        profit =0
        buy=0
        for i in range(1,len(prices)):
            if prices[i]-prices[buy]>profit:
                profit=prices[i]-prices[buy]
            else:
                if prices[i]<prices[buy]:
                    buy=i


        return profit