class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_prices=prices[0]
        profit=0
        for price in prices:
            if price < min_prices:
                min_prices=price
            current_profit=price-min_prices
            if current_profit>profit:
                profit=current_profit
        return profit
