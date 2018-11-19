# C24
To verify whether 24 is really a good number for the game described in https://siufuhon.blogspot.com/2018/11/24.html.
The program assumes that 4 numbers are randomly drawn from a standard deck of 52 cards.

Directory structure
* c24.py -- main program
* analysis.xlsx -- analysis file

Program execution:
With Python 3+, run "python c24.py"

c24_improved.py updates c24.py to address the following problem:
In cn24.py, the statistics are collected assuming that the picked numbers have to be used in the order that they are picked. This may wrongly flag a particular permutation not be able to generate particular values, thus underestimating the percentage of combinations that can generate particular values. 
The respective statistics are stored in analysis_improved.xlsx.