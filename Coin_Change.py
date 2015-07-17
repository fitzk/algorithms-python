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

	#brute force divide and conquer algorithm
	def changeslow(self,coins, amount):
		#if there is a K-cent coin then that one coin is the minimum


		# j=0
		# while j < len(coins):
		# 	if coins[j] == amount:
		# 		print coins[j]
		# 		return coins[j]
		# 	j=j+1
		i=1

		while i <= amount:
			print i
			print amount
		 	coins_a = self.changeslow(coins, i)
			coins_b = self.changeslow(coins, amount - i)
			print "Coints at a: "
			print coins_a
			i = i + 1
		if amount == 1:
			return 1
		#
		# 	new_coins = coins_a + coins_b
		# 	print new_coins
		# 	i = i +1
		# return "fin"





	#Greedy algorithm
	def changegreedy(self, V, A):
    		coinUsed = []  # type of coins used
    		m = 0  # minimum number of coins used

    		# reverses V to be in decreasing order
    		length = len(V) - 1
    		while length >= 0:
        		if A > V[length] or A == V[length]:
        			A = A - V[length]
        			m = m + 1
            			coinUsed.append(V[length])

        		elif A < V[length]:
            			length = length - 1

        	return m, coinUsed

    	#coin denomination using dynammic programming
	def coinDen(self, coins, amount):
		table = []    #table to keep tarck of number of coins
    		coinUsed = []  #table to keep tarck of coins used

    		for i in range(0, amount + 1):
        		table.append(i)
        		coinUsed.append(1)

    		for i in coins:
        		for j in range(i, amount + 1):
            			if table[j] > table[j - i] + 1:
                			table[j] = table[j - i] + 1
                			coinUsed[j] = i

    		return table[amount], coinUsed
