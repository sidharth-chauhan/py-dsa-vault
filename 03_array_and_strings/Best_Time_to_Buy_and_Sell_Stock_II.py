'''
🔢 leetcode 122: Best Time to Buy and Sell Stock II
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''

def maxProfit(self, prices):
        profit=0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                profit=profit+(prices[i]-prices[i-1])
        return profit