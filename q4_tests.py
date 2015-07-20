######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 2                                          #
# File:           q4_tests.py                                        #
# Description:    Test greedy and dp algorithms for runtimes         #
######################################################################
#!/usr/bin/env python
from Coin_Change import Coin_Change
import time
import sys
import re

coins = []
coinArr = []
coin_change = Coin_Change()
array = [1,5,10,25,50]
amount = 2010

f2 = open('q4_results.txt','w')

while amount <= 2200:
    s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'
    f2.write(s)

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    ln = amount
    while ln > 0:
        coinArr.append(coins[ln])
        ln = ln - coins[ln]

    #Write to file results of dynamic programming algorithm
    s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coinArr) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(s)

    #empty arr
    del coins[:]
    coins[:] = []

    del coinArr[:]
    coinArr[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(s)

    #empty arr
    del coins[:]
    coins[:] = []

    amount = amount + 5

f2.close()
