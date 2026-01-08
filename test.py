# class Solution:
#     def maxProfit(self, prices) -> int:
#         l, r = 0, 1
#         maxP = 0

#         while r < len(prices):
            
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(maxP, profit)
#             else:
#                 l = r
#             r += 1
#         return maxP
        

# obj = Solution()
# prices = [10,1,5,6,7,1]

# res=obj.maxProfit(prices)
# print(f'\n res:{res}\n')
s='kha s'
print(list(s))