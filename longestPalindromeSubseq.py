#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:42:17 2023

@author: shivanipal
"""


'''
PROBLEM STATEMENT: 
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting
some or no elements without changing the order of the remaining elements.

leetcode link: https://leetcode.com/problems/longest-palindromic-subsequence/

'''

def longestPalindromeSubseq(s: str) -> int:
    
    str_len = len(s)
    
    dp = [[0] * str_len for c in range(str_len)]
    
    for i in range(str_len - 1, -1, -1):
        
        dp[i][i] = 1
        for j in range(i+1, str_len):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    length  = dp[0][str_len - 1]
    
    return length


