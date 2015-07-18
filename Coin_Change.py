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
    # This implementation is called changeslow.
    # To make change for A cents:
    # If there is a K-cent coin, then that one coin is the minimum
    # Otherwise, for each value i < K,
    # Find the minimum number of coins needed to make i cents
    # Find the minimum number of coins needed to make K - i cents
    # Choose the i that minimizes this sum
    # This algorithm can be viewed as divide-and-conquer, or as brute force. This solution is very recursive and runs in exponential time.
    
    def changeslow(coins,change, coinUsed):
        min_coins = change
    
        #base case if chnage is equal to one of the coin
        if change in coins:
            coinUsed[change] = change
            return 1, arr
    
        #make recursive call to find number of coins
        else:
            for c in range(0, len(coins)): 
                if coins[c] <= change:
                    num_coins = 1 + changeslow(coins,change-coins[c], arr)[0]
                
                    if num_coins < min_coins:
                        min_coins = num_coins
    
        return min_coins, coinUsed
    
    #Greedy algorithm
    def changegreedy(V, A):
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
