#Dictionnary
# return profit

import math

profit = {
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}

profit_val = round((profit['sell_price']-profit['cost_price'])*profit['inventory'])

print(profit_val)
