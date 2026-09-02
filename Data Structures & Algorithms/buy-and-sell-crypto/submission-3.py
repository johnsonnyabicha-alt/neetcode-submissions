class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxP = 0
        while r < len(prices): # so we can go through the whole list, with out getting out of index
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

