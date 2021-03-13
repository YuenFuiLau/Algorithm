import numpy as np


def inf_MaxProfit(prices):


    dp_i_0 = 0
    dp_i_1 = -max(prices)-5

    for stock in prices:

        prev_dp_0 = dp_i_0

        dp_i_0 = max(dp_i_0,dp_i_1 + stock)
        dp_i_1 = max(dp_i_1,prev_dp_0 - stock)
        

    return dp_i_0



def maxProfit(prices,k=2):

    if len(prices) == 0:

        return 0


    dp = np.zeros((len(prices),k+1,2))

    if 2*k > len(prices):

        return inf_MaxProfit(prices)

    

    for j in range(1,k+1):
        

        for i in range(len(prices)):

            if i - 1 < 0:

                dp[i][j][0] = 0
                dp[i][j][1] = -prices[i]

                continue

            dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])

            dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i])


    return dp[len(prices)-1][2][0]


a =  [0,5,0,3]

a =  [3,3,5,0,0,3,1,4]

b = [7,1,5,3,6,4]

b = [3,2,6,5,0,3]

c = []

test = inf_MaxProfit(b)

test_er = maxProfit(c)

ans = maxProfit(a)

dp = np.zeros((2,1,2))

a =  [3,3,5,0,0,3,1,4]


