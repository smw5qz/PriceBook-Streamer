# PriceBook-Streamer
Streams a stock's pricebook from Robinhood, continously scores the balance -1 to 1, with an expoentially weighted sum through the depth of both sides of the book.

The balance score is graphed against the latest trade price, and the frequency depends on connection speed and potential rate limits with Robinhood. Intended as an exploratory tool for assessing correlation/causation in supply/demand levels and subsequent price action.

Please note that order spoofing, flash, and related tactics can obscure the true supply/demand levels. A deeper dive would require also streaming time&sales to see which orders filled.
