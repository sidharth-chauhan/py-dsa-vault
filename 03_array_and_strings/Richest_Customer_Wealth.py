'''
🔢 leetcode 1672: Richest Customer Wealth
link: https://leetcode.com/problems/richest-customer-wealth/
'''


def maximumWealth(self, accounts):
        welth=0
        for i in accounts:
            k=0
            for j in range(len(i)):
                k=k+i[j]
            if k>welth:
                welth=k
        return welth
