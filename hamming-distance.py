#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 02:39:29 2023

@author: shivanipal
"""

# # O(n^2)
# def get_distance(arr):
#         sum_of_pair_distances =0
#         for i in arr:
#             for j in arr:
#                 # bitwise operation works on binary representation of integer
#                 # XOR -> 1 only when both operand bits are different
#                 xor = i ^ j
#                 dist = 0
#                 # Maximum woukld be 8 loops since input size is is limited to 256
#                 while( xor>0 ):
#                     lsb = xor & 1
#                     # number of different bits
#                     dist+= lsb
#                     xor = xor >> 1
#                 sum_of_pair_distances+=dist
#         return sum_of_pair_distances
       

# O(8n) = O(n)
def get_distance(arr):
        n = len(arr)
        sum_of_pair_distances = 0
        for i in range(8):
            #number of 1's at ith bit
            count1 = 0
            for num in arr:
                # right shift and & bitwise operator to check if ith bit is 1
                if (num>>i) & 1:
                    count1 +=1
            sum_of_pair_distances += count1*(n-count1)
        return sum_of_pair_distances*2
 
