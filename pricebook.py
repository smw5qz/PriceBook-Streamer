#stream supply/demand for any symbol from pricebook

import robin_stocks as rs
import time as t
import numpy as np
import math as m
from matplotlib import pyplot as plt

rs.robinhood.authentication.login(username='XXX', password='XXX', expiresIn=86400, scope='internal', by_sms=True, store_session=True, mfa_code=None, pickle_name='')

symbol = 'SPY'
prices = []
imbalances = []
i = 0
j = 200

#continuously read pricebook, may be altered for rate limits
while i < j:

    i += 1

    #get pricebook
    level2 = rs.robinhood.stocks.get_pricebook_by_symbol(symbol, info=None)

    #get current price
    price = rs.robinhood.stocks.get_latest_price(symbol, priceType=None, includeExtendedHours=True)
    prices.append(float(price[0]))

    #compute weighted sum on bids and asks, then calculate imbalance
    total = [0,0]
    side_sum = [0,0]
    imbalance = 0    
    sides = ['bids','asks']

    for x in range(len(sides)):
        
        side_sum[x] = sum([m.exp(-0.5 * y) * level2[sides[x]][y]['quantity'] for y in range(len(level2[sides[x]]))])

    imbalance = round(((side_sum[0] - side_sum[1]) / (side_sum[0] + side_sum[1])),2)
    imbalances.append(imbalance)

    print(round(imbalance,2), float(price[0]))  

plt.subplot(2,1,1)
plt.plot(prices)
plt.subplot(2,1,2)
plt.plot(imbalances)
plt.show()
