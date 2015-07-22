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
import xlsxwriter

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

f = xlsxwriter.Workbook('r6_results.xlsx')
f2 = f.add_worksheet('Question 6')
f3 = f.add_worksheet('Question 5b')
f4 = f.add_worksheet('Question 5a')
f5 = f.add_worksheet('Question 4')
bold = f.add_format({'bold': True})

f2.write('B1', 'DP', bold)
f2.write('D1', 'Greedy', bold)
f2.write('F1', 'Recursive', bold)
f2.write('A2', 'Amount', bold)
f2.write('B2', 'Coin Used', bold)
f2.write('C2', 'Time', bold)
f2.write('D2', 'Coin Used', bold)
f2.write('E2', 'Time', bold)
f2.write('F2', 'Coin Used', bold)
f2.write('G2', 'Time', bold)

f3.write('B1', 'DP', bold)
f3.write('D1', 'Greedy', bold)
f3.write('F1', 'Recursive', bold)
f3.write('A2', 'Amount', bold)
f3.write('B2', 'Coin Used', bold)
f3.write('C2', 'Time', bold)
f3.write('D2', 'Coin Used', bold)
f3.write('E2', 'Time', bold)
f3.write('F2', 'Coin Used', bold)
f3.write('G2', 'Time', bold)

f4.write('B1', 'DP', bold)
f4.write('D1', 'Greedy', bold)
f4.write('F1', 'Recursive', bold)
f4.write('A2', 'Amount', bold)
f4.write('B2', 'Coin Used', bold)
f4.write('C2', 'Time', bold)
f4.write('D2', 'Coin Used', bold)
f4.write('E2', 'Time', bold)
f4.write('F2', 'Coin Used', bold)
f4.write('G2', 'Time', bold)

f5.write('B1', 'DP', bold)
f5.write('D1', 'Greedy', bold)
f5.write('F1', 'Recursive', bold)
f5.write('A2', 'Amount', bold)
f5.write('B2', 'Coin Used', bold)
f5.write('C2', 'Time', bold)
f5.write('D2', 'Coin Used', bold)
f5.write('E2', 'Time', bold)
f5.write('F2', 'Coin Used', bold)
f5.write('G2', 'Time', bold)

row = 2
col = 0
while amount <= HIGH:
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(row,col,amount)
    f2.write(row,col+1, coinUsed)
    f2.write(row,col+2,end-start)

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(row,col+3, coinUsed)
    f2.write(row,col+4,end-start)
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
    f2.write(row,col+5, coinUsed)
    f2.write(row,col+6,end-start)

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
    row = row + 1
    amount = amount + DIFFERENCE

array = [1,2,6,12,24,48,60]
print array
amount = START
row = 2
col = 0
while amount <= HIGH:
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f4.write(row,col,amount)
    f4.write(row,col+1, coinUsed)
    f4.write(row,col+2,end-start)

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f4.write(row,col+3, coinUsed)
    f4.write(row,col+4,end-start)
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
    f4.write(row,col+5, coinUsed)
    f4.write(row,col+6,end-start)

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
    row = row + 1
    amount = amount + DIFFERENCE

array = [1,6,13,37,150]
print array
amount = START
row = 2
col = 0
while amount <= HIGH:
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f3.write(row,col,amount)
    f3.write(row,col+1, coinUsed)
    f3.write(row,col+2,end-start)

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f3.write(row,col+3, coinUsed)
    f3.write(row,col+4,end-start)
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
    f3.write(row,col+5, coinUsed)
    f3.write(row,col+6,end-start)

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
    row = row + 1
    amount = amount + DIFFERENCE
    
array = [1,5,10,25,50]
print array
amount = START
row = 2
col = 0
while amount <= HIGH:
    #s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'

    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f5.write(row,col,amount)
    f5.write(row,col+1, coinUsed)
    f5.write(row,col+2,end-start)

    #empty arr
    del coins[:]
    coins[:] = []

    # greedy algorithm
    start = time.clock()
    coinUsed, coins = coin_change.changegreedy(array, amount) # function to be tested
    end = time.clock()

    #Write to file results of greedy algorithm
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f5.write(row,col+3, coinUsed)
    f5.write(row,col+4,end-start)
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
    f5.write(row,col+5, coinUsed)
    f5.write(row,col+6,end-start)

    #empty arr
    del coinsNeeded[:]
    coinsNeeded[:] = []
    row = row + 1
    amount = amount + DIFFERENCE

f.close()
