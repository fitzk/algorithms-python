######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 2                                          #
# File:           runtime_tests.py                                   #
# Description:    Calculates runtimes for algorithms                 #
######################################################################
#!/usr/bin/env python
from Coin_Change import Coin_Change
import time
import sys
import re
import csv

coins = []
coinArr = []
coin_change = Coin_Change()

START = 10 #Starting amount of change needed
HIGH = 20  #Amount Upto change needed
DIFFERENCE = 5  #Interval for increment of change

array = [1]
n = 2
while n < 31:
    array.append(n)
    n = n + 2
print array
amount = START

f2 = csv.writer(open("Q6.csv", "wb"))
f3 = csv.writer(open("5b.csv", "wb"))
f4 = csv.writer(open("5a.csv", "wb"))
f5 = csv.writer(open("Q4.csv", "wb"))
head = ['amount', 'dp coin used', 'dp time', 'greedy coin used', 'greedy time', 'rec coin used', 'rec time'] 

f2.writerow(head)
f3.writerow(head)
f4.writerow(head)
f5.writerow(head)

while amount <= HIGH:
 
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'
    data = []
    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(amount))
    data.append(str(coinUsed))
    data.append(str(end-start))

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
    #empty arr
    del coins[:]
    coins[:] = []
     
    # brute-force algorithm
    coinsNeeded = [0]*(len(array))
    start = time.clock()
    coinUsed, coinsNeeded = coin_change.changeslow(array, amount, coinsNeeded) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'Brute Force' + '\n' + 'Coins used:'+ str(coinsNeeded) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
    f2.writerow(data)
    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
  
    amount = amount + DIFFERENCE

array = [1,2,6,12,24,48,60]
print array
amount = START
row = 2
col = 0
while amount <= HIGH:
    data = []
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(amount))
    data.append(str(coinUsed))
    data.append(str(end-start))

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
     #empty arr
    del coins[:]
    coins[:] = []
    
    # brute-force algorithm
    coinsNeeded = [0]*(len(array))
    start = time.clock()
    coinUsed, coinsNeeded = coin_change.changeslow(array, amount, coinsNeeded) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'Brute Force' + '\n' + 'Coins used:'+ str(coinsNeeded) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
    f4.writerow(data)

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
 
    amount = amount + DIFFERENCE

array = [1,6,13,37,150]
print array
amount = START

while amount <= HIGH:
    data = []
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(amount))
    
    data.append(str(coinUsed))
    data.append(str(end-start))

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
     #empty arr
    del coins[:]
    coins[:] = []
    
    # brute-force algorithm
    coinsNeeded = [0]*(len(array))
    start = time.clock()
    coinUsed, coinsNeeded = coin_change.changeslow(array, amount, coinsNeeded) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'Brute Force' + '\n' + 'Coins used:'+ str(coinsNeeded) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
    f3.writerow(data)

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
   
    amount = amount + DIFFERENCE
    
array = [1,5,10,25,50]
print array
amount = START

while amount <= HIGH:
    data = []
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(amount))
    data.append(str(coinUsed))
    data.append(str(end-start))

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
     #empty arr
    del coins[:]
    coins[:] = []
        
    # brute-force algorithm
    coinsNeeded = [0]*(len(array))
    start = time.clock()
    coinUsed, coinsNeeded = coin_change.changeslow(array, amount, coinsNeeded) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'Brute Force' + '\n' + 'Coins used:'+ str(coinsNeeded) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    data.append(str(coinUsed))
    data.append(str(end-start))
    f5.writerow(data)

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
  
    amount = amount + DIFFERENCE

