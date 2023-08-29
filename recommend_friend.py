# dp
def recommendFriends(n, connections):
  # Initialize adjacency list for each user
  adj = [set() for _ in range(n)]
  
  # Initialize dp list for each user
  # Each entry is a list containing [maximum_common_friends, user_with_maximum_common_friends]
  # and a Counter to store the count of common friends with other users
  dp = [[[-1, 1], Counter()] for _ in range(n)]
  
  # Iterate through the list of connections
  for i, j in connections:
      # Add each user to the adjacency list of the other user
      adj[j].add(i)
      adj[i].add(j)
  
  # Iterate through the list of connections again and add mutual friends' counts to dp
  for i, j in connections + [[w, v] for v, w in connections]:
      for k in adj[j]:
          if k != i and k not in adj[i]:
              # Increment the count of common friends using a Counter
              dp[i][1][k] += 1
              dp[k][1][i] += 1
  
              # Update the maximum_common_friends and user_with_maximum_common_friends values
              # for both users i and k
              dp[i][0] = max([dp[i][1][k], -k], dp[i][0])
              dp[k][0] = max([dp[k][1][i], -i], dp[k][0])
  
  # Return a list containing the recommended friend for each user
  # The recommended friend is the user with the maximum_common_friends
  # The friend's index is stored as -user_index in the dp list
  recommended_friends = [-dp[i][0][1] for i in range(n)]
