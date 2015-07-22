######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 2                                          #
# File:           test_coin.py                                       #
# Description:    Test coin change algorithms for correctness        #
######################################################################
from Coin_Change import Coin_Change

import sys
import re

array = []
coinUsed = 0
coins = []
coinArr = []
coin_change = Coin_Change()
#creates a file object for input and output

fileName = 'coins.txt'
if len(sys.argv) > 1:
    fileName = sys.argv[1]
outFile = fileName[:-4] + 'change.txt'

try:
    f = open(fileName,'r')
except IOError:
    print 'Error in opening file coins.txt'
    sys.exit(-1)

f2 = open(outFile,'w')
line = f.readline()
while line:
    array =  map(int, re.findall(r"[-+]?\d*\-\d+|\d+", line))
    amount = int(f.readline())
    line = f.readline()
    
    # dynamic programming algorithm
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    print coins
    #Write to file results of dynamic programming algorithm
    s = str(coins) + '\n' + str(coinUsed) + '\n' 
    f2.write(s)

    #empty arr
    del coins[:]
    coins[:] = []
    
    # greedy algorithm
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    print coins
    
    #Write to file results of greedy algorithm
    s = str(coins) + '\n' + str(coinUsed) + '\n'
    f2.write(s)
    
    #empty arr
    del coins[:]
    coins[:] = []
  
    coinsNeeded = [0]*(len(array))
    
    # brute-force algorithm
    coinUsed, coinNeeded = coin_change.changeslow(array, amount, coinsNeeded) # function to be tested
    
    #Write to file results of brute-force algorithm
    s = str(coinNeeded) + '\n' + str(coinUsed) + '\n' 
    f2.write(s)
    print coinsNeeded
    
    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
    
    del array[:]
    array[:] = []

# close file
f.close()
f2.close()
