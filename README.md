Project Group 1
project1_CS325
Project 2 Analysis of Algorithms Summer 2015

This program is implementation of coin change problem using 3 different algorithms to do running time analysis for these 3 
algorithms. 
HOW TO USE: There are 3 files needed for this program. 4th file is optional coins.txt
1. Coin_Change.py : This is python module contains a python object Coin_Change. All the 4 algorithms are methods of 
this object. 
2. test_coin.py : This is python script which tests the correctness of all 3 algorithms and saves the results in file 
[inputfile]change.txt. The input is given in command line as file name [inputfile].txt by user. This same input file name
is used as prefix to output file change.txt. If no command line input found default file coins.txt will be used
3. runtime_tests.py : This is python script which calculates the running for each algorithm for different coins denominations
and different amount. It is recommended don't use amount over 45 if recursive algorithm is included. Comment out recursive part
to run test for higher amount.
4. coins.txt: This file will be used as default input if no command line argument is given for test_coin.py. 
NOTE: Input file is only needed for test_coin.py
