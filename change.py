######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 2                                          #
# File:           change.py                                          #
# Description:    Object that contains three algorithms that solve   #
#                 the coin change problem                            #
######################################################################
class change(object):
	
	#Greedy algorithm
	def changegreedy(self, V, A):
		temp1 = []  # temp V in reverse (decreasing order)
    		temp2 = []  # temp counter for each coin used (decreasing order)
    		C = []  # number of each coin used (increasing order)
    		m = 0  # minimum number of coins used

		# reverses V to be in decreasing order
    		for i in range((len(V)), 0, -1):
        		temp1.append(V[i-1])

		# start each counter at 0
    		for i in range(0, len(V)):
        		temp2.append(0)

		# greedy algorithm to make change
    		while A != 0:
        		for i in range(0, len(V)):
            			if temp1[i] <= A:
					A -= temp1[i]	
					temp2[i] += 1		
					m += 1
                			break

		# store reverse of temp2 in C
    		for i in range((len(temp2)), 0, -1):
        		C.append(temp2[i-1])

    		print C
    		print m
