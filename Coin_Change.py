######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 2                                          #
# File:           Coin_Change.py                                     #
# Description:    Object that contains three algorithms that solve   #
#                 the coin change problem                            #
######################################################################

class Coin_Change(object):
    # brute force divide and conquer algorithm
    def changeslow(self, coins, change, coinUsed):
        min_coins = change

        #base case if chnage is equal to one of the coin
        if change in coins:
            coinUsed[change] = change
            return 1, coinUsed

        #make recursive call to find number of coins
        else:
            for c in range(0, len(coins)):
                if coins[c] <= change:
                    num_coins = 1 + self.changeslow(coins,change-coins[c], coinUsed)[0]

                    if num_coins < min_coins:
                        coinUsed[change] = coins[c]
                        min_coins = num_coins

        return min_coins, coinUsed

    #Greedy algorithm
    def changegreedy(self, V, A):
        coinUsed = []  # type of coins used
        m = 0  # minimum number of coins used

        # reverses V to be in decreasing order
        length = len(V) - 1
        while length >= 0 and A != 0:

            m = m + A/V[length]

            for i in range(0, A/V[length]):
                coinUsed.append(V[length])

            A = A % V[length]

            length = length - 1

        return m, coinUsed

    # coin denomination using dynammic programming
    def coinDen(self, coins, amount):
        table = []  # table to keep tarck of number of coins
        coinUsed = []  # table to keep tarck of coins used

        for i in range(0, amount + 1):
            table.append(i)
            coinUsed.append(1)

        for i in coins:
            for j in range(i, amount + 1):
                if table[j] > table[j - i] + 1:
                    table[j] = table[j - i] + 1
                    coinUsed[j] = i

        return table[amount], coinUsed
