# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:37:09 2020

@author: franc
"""

s = "DATAMININGSAPIENZA" # defined Sequence
nalgo4 = len(s)

## creating a table of rows and column equal to len of string
DST= [[0 for i in range(nalgo4)]for i in range (nalgo4)]

# for all values where length of sub sequence is 1
for i in range (nalgo4):
    DST[i][i] = 1
    
# for all values where length of subsequence is more than 1
# we make a loop for the lengths of sub-sequence    
for sseq in range(2, nalgo4+1): 
    for i in range(nalgo4-sseq+1):
        j = i+sseq-1
        if (s[i] == s[j] and sseq == 2): #conditioning for length 2 subsequences
            DST[i][j] = 2
        elif s[i] == s[j]:  #conditioning for all sseq greater than 2
            DST[i][j] = DST[i+1][j-1] + 2
        else:
            DST[i][j] = max(DST[i][j-1], DST[i+1][j])

print("The Longest Palindromic sub Sequence is ", DST[0][nalgo4-1])
