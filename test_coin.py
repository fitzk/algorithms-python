######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 2                                          #
# File:           test_coin.py                                       #
# Description:    Test coin change algorithms for correctness        #
######################################################################
from Coin_Change import Coin_Change

import time
import sys
import re

array = []
coinUsed = 0
coins = []
coinArr = []
coin_change = Coin_Change()
#creates a file object for input and output
try:
    f = open(sys.argv[1],'r')
except IOError:
    print 'Error in opening input file'
    sys.exit(-1)

f2 = open('change.txt','w')
line = f.readline()
while line:
    array =  map(int, re.findall(r"[-+]?\d*\-\d+|\d+", line))
    amount = int(f.readline())
    line = f.readline()

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

    # coinsNeeded = [1]*(amount + 1)

    # brute-force algorithm
    # start = time.clock()
    # coinUsed, coinsNeeded = coin_change.changeslow(array, amount, coinsNeeded) # function to be tested
    # end = time.clock()

    # ln = amount
    # while ln > 0:
        # coinArr.append(coinsNeeded[ln])
        # ln = ln - coinsNeeded[ln]

    #Write to file results of brute-force algorithm
    # s = 'brute-force algorithm' + '\n' + 'Coins used:' + str(coinArr) + '\n' + 'Number of coins:' + str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    # f2.write(s)

    # del coinArr[:]
    # coinArr[:] = []

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []

    del array[:]
    array[:] = []

# close file
f.close()
f2.close()
