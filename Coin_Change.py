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
    
    # brute force divide and conquer algorithm
    def changeslow(self, coins, change, coinUsed):
	    amount = change
	    arr = [1]*(change+1)
	    coinNum, arr = self.changeslowRec(coins, change, arr)
        while amount > 0:
		    index = coins.index(arr[amount])
		    coinUsed[index] = coinUsed[index] + 1
		    amount = amount - arr[amount]

        return coinNum, coinUsed
    
    def changeslowRec(self, coins, change, coinUsed):
        min_coins = change

        #base case if chnage is equal to one of the coin
        if change in coins:
            coinUsed[change] = change
            return 1, coinUsed

        #make recursive call to find number of coins
        else:
            for c in range(0, len(coins)):
                if coins[c] <= change:
                    num_coins = 1 + self.changeslowRec(coins,change-coins[c], coinUsed)[0]

                    if num_coins < min_coins:
                        coinUsed[change] = coins[c]
                        min_coins = num_coins

        return min_coins, coinUsed
    
    #Greedy algorithm
    def changegreedy(self, V, A):
        coinUsed = [0]*len(V)  # type of coins used 
        m = 0  # minimum number of coins used

        # reverses V to be in decreasing order
        length = len(V) - 1
        while length >= 0 and A != 0:
        
            m = m + A/V[length]
            
            for i in range(0, A/V[length]):
                coinUsed[length] = coinUsed[length] + 1
            
            A = A % V[length]
            
            length = length - 1
    
        return m, coinUsed

   # coin denomination using dynammic programming
    def coinDen(self, coins, amount):
        table = []  # table to keep tarck of number of coins
        coinUsed = []  # table to keep tarck of coins used
	    c = [0]*len(coins)  # table to keep tarck of coins used

        for i in range(0, amount + 1):
            table.append(i)
            coinUsed.append(1)

        for i in coins:
            for j in range(i, amount + 1):
                if table[j] > table[j - i] + 1:
                    table[j] = table[j - i] + 1
                    coinUsed[j] = i
	    ln = amount
        while amount > 0:
		    index = coins.index(coinUsed[amount])
		    c[index] = c[index] + 1
		    amount = amount - coinUsed[amount]

        return table[ln], c
