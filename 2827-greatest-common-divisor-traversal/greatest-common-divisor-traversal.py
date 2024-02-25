class Solution:
    def find_parent(self, parent, x):
        return x if parent[x] == x else self.find_parent(parent, parent[x])

    def union(self, parent, size, x, y):
        x = self.find_parent(parent, x)
        y = self.find_parent(parent, y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]

    def canTraverseAllPairs(self, nums):
        n = len(nums)
        if n == 1:
            return True
        
        parent = [i for i in range(n)]
        size = [1] * n
        factor_index = {}
        
        for i, x in enumerate(nums):
            if x == 1:
                return False
            
            for factor in range(2, int(x**0.5) + 1):
                if x % factor == 0:
                    if factor in factor_index:
                        self.union(parent, size, i, factor_index[factor])
                    else:
                        factor_index[factor] = i
                    while x % factor == 0:
                        x //= factor 
            
            if x > 1:
                if x in factor_index:
                    self.union(parent, size, i, factor_index[x])
                else:
                    factor_index[x] = i
        
        return size[self.find_parent(parent, 0)] == n

    


        # n = len(nums)
    
        # def dfs(curr, visited):
        #     visited[curr] = True
            
        #     for i in range(n):
        #         if not visited[i] and gcd(nums[curr], nums[i]) > 1:
        #             dfs(i, visited)
                    
        # for i in range(n):
        #     visited = [False] * n
        #     dfs(i, visited)
            
        #     if not all(visited):
        #         return False
                
        # return True
        