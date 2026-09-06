class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxPossibleProfit = 0

        minPrice = prices[0]

        for price in prices:

            minPrice = min(price,minPrice)

            maxPossibleProfit= max(maxPossibleProfit, price-minPrice)

        return maxPossibleProfit