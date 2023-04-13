
'''

Confusing Configuarations
A configuaration is defined by four digits. Each digit can take values from zero to nine.You can move from one configuaration to the next configuaration by changing the only one of the four digits(to its successor or predcessor). Let say you are in configuaration 5297, the feasible next configuarations are 5397, 5197,5207, 5287, 4297, 5298 etc. Observe that sucessor(9) = 0 , predecssor(0) = 9 There are configuarations which are forbidden that means you cannot enter the configuaration. Given a start configuaration , end configuaration & forbidden configuarations write a program to find the minimum number of moves to reach the end configuaration.

NOTE: The starting, ending and forbidden combinations must be passed as strings and not integers, the output is an integer. This is depicted in the below examples.

def number_of_moves(start_config, end_config, forbidden_config):
  
  
  
  return min_moves
Example1:

Input:
start_config = '9999'
end_config = '0000'
forbidden_configs = ['5189' ,'5123']
Output:
min_moves = 4
Example2:

Input:
start_config = '9999'
end_config = '0000'
forbidden_configs = ['0000', '1111']
Output:
min_moves = -1

'''

from collections import deque

def number_of_moves(start_config, end_config, forbidden_configs):

    """
    
    start_config: initial state of the cofiguration
    end_configuration: desired state of configuration
    forbidden configuration: configuration cannot enter

    return: minimum number of moves to reach the end configurations

    logic: we solve it using breadth first algorithm
        We start from the initial configuration and explore other configuration 
        changing one configuration at a time
        We keep note of visited configs and forbidden configs
        Stop when reach end config or explored all configs
    
    """

    # we make a foridden configuration set and visited set, both to be handled similarly
    forbidden_configs_set = set(forbidden_configs)
    # visisted set
    visited = set()

    # Initialize a double ended queue for the BFS, and we insert the starting configuration and level
    queue = deque([(start_config, 0)])

    # while nodes in queue, iterate
    while queue:

        # pop the first node from the queue
        curr_conf, curr_move = queue.popleft()

        # if current configuration is the needed end_config, we return the current move number
        if curr_conf == end_config:
            return curr_move
        
        # if the current conf hasalready been visited or is in forbidden set, continue the loop 
        if curr_conf in visited or curr_conf in forbidden_configs_set:
            continue
        
        # add the curr_conf to the viisted set
        visited.add(curr_conf)

        # iterate for all digits in the conf
        for i in range(4):
            
            # we find the next conf digit, and handle the 0->9 and 9->0 by using % operator. 

            # consider the digit = int(curr_conf[i])
            #  (digit+1)%10, if the value of digit is 9, then adding 1 to it would result in 10 and 10 modulo 10 is 0
            #  (digit-1)%10, if the value of digit is 0, then subtracting 1 from it would result in -1 and -1 modulo 10 is 9
            next_digit_in_conf = [(int(curr_conf[i])-1)%10, (int(curr_conf[i])+1)%10]
            
            # fnd new confs and store it in the quueu
            for digit in next_digit_in_conf:
                # find the new conf
                new_conf = curr_conf[:i] + str(digit) + curr_conf[i+1:]

                # append new conf in the queue with updated level
                queue.append((new_conf, curr_move+1))
    # return -1 incase the configuration is not reachable 
    return -1 
