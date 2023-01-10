class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_val = float("inf")
        
        max_profit = 0
        
        for val in prices:
            
            if val <= max_val:
                max_val = val
            else:
                if val - max_val > max_profit:
                    max_profit = val - max_val 
        return max_profit        