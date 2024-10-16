def maxProfit_bruteforce (prices):
   max_price = 1

   for i, price in enumerate(prices):
       for j in range(i, len(prices)):
           max_price = max(prices[j] - price, max_price)
           max_price = max(prices[j] - price, max_price)

   return

