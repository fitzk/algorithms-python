######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 2                                          #
# File:           runtime_tests.py                                   #
# Description:    Test greedy and dp algorithms for runtimes         #
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
array = [1,5,10,25,50]
amount = 100010

f = xlsxwriter.Workbook('runtimes.xlsx')
f2 = f.add_worksheet('Question 4')
bold = f.add_format({'bold': True})

f2.write('B1', 'DP', bold)
f2.write('D1', 'Greedy', bold)
f2.write('A2', 'Amount', bold)
f2.write('B2', 'Coin Used', bold)
f2.write('C2', 'Time', bold)
f2.write('D2', 'Coin Used', bold)
f2.write('E2', 'Time', bold)

row = 2
col = 0
while amount <= 100110:
    s = 'Coins Available:' + str(array) + '\n' + 'Change needed:' + str(amount) + '\n' + '\n'


    # dynamic programming algorithm
    start = time.clock()
    coinUsed, coins = coin_change.coinDen(array, amount) # function to be tested
    end = time.clock()

    ln = amount
    while ln > 0:
        coinArr.append(coins[ln])
        ln = ln - coins[ln]

    #Write to file results of dynamic programming algorithm
    # s = 'dynamic programming algorithm' + '\n' + 'Coins used:'+ str(coinArr) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(row,col,amount)
    f2.write(row,col+1, coinUsed)
    f2.write(row,col+2,end-start)

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
    # s = 'greedy algorithm' + '\n' + 'Coins used:' + str(coins) + '\n' + 'Number of coins:'+ str(coinUsed) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(row,col+3, coinUsed)
    f2.write(row,col+4,end-start)
    row = row + 1

    #empty arr
    del coins[:]
    coins[:] = []

    amount = amount + 1

f.close()
