'''
 
Agent 007 has stumbled upon a coded message that could lead to a top-secret document. 
The message is in the form of a string of digits, and it is suspected that the digits represent a series of numbers that form a combination to a lock securing the document.

However, the message is coded in such a way that it is missing vital information - there are no spaces between the digits, making it impossible to determine the correct combination. 
All that is known is that the combination consists of numbers between 1 and M, with no leading zeros and stay in the same order as the numbers presented in the given code.

Assist the agent's task by determining the number of possible combinations that can be represented by the coded message. 
As this is a matter of national security, the answer must be provided modulo 10^9 + 7 to ensure that it remains confidential.

def num_combinations(code, M):
    -- your code ----
    return number_of_combinations_possible
Example 1:

Input: code = "3129", M = 4000
Output: 8
Explanation: There are 8 possible array combinations that can formed using the input such that all numbers are smaller or equal to M. 
[3129],[312,9],[31,29],[3,129],[31,2,9],[3,12,9],[3,1,29],[3,1,2,9]
Example 2:

Input: code = "2000", M = 20
Output: 0 
Explanation: There are 0 possible ways to create an array from the code that will satisfy our conditions. Since, 0 is not allowed in the numbers as the combination only consists of numbers between 1 and M. 
Example 3:

Input: code = "500", M = 1000
Output: 1
Explanation: [500] is the only array possible since, numbers have to be between 1 and M. 
    
    '''
    
    
def num_combinations(code, M):
    count = 0
    
    s = []
    # find all combinations
    def comb(string):
        # check for partitions 
        for partitions in range(1 << (len(string)-1)):
            result = []
            prevcut = 0
            # find the combimatios fro  the fillowin range
            for i in range(len(string)-1):
                if (1<<i) & partitions != 0:

                    result.append(string[prevcut:(i+1)])
                    prevcut = i+1
            # append tp result
            result.append(string[prevcut:])
            # retur the arrayb of all the combinations 
            yield result

    # iterate for al cobinations and check if all eements are less than the target M
    for partition in comb(code):
        # Flaf set to true,will become false when ekement greater tahn M
        flag = True
        for i in partition:
            # confition for false
            if int(i) > M:
                flag = False
        if flag:
            count+=1

    # return count
    return count

code = "3129"
M = 4000
print(num_combinations(code, M))
