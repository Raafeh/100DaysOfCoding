from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Initialize the dictionary to store directly connected cities for each city
        connections = {i: set() for i in range(n)}
        
        # Populate the dictionary based on the given roads
        for road in roads:
            connections[road[0]].add(road[1])
            connections[road[1]].add(road[0])
        
        # Initialize the maximal network rank
        max_network_rank = 0
        
        # Iterate through all pairs of cities
        for city1 in range(n):
            for city2 in range(city1 + 1, n):
                # Calculate the network rank for the current pair
                network_rank = len(connections[city1]) + len(connections[city2])
                if city2 in connections[city1]:
                    network_rank -= 1  # Subtract 1 if there's a direct road between them
                
                # Update the maximal network rank
                max_network_rank = max(max_network_rank, network_rank)
        
        return max_network_rank

# Testcases:
solution = Solution()
n1 = 4
roads1 = [[0,1],[0,3],[1,2],[1,3]]
print(solution.maximalNetworkRank(n1, roads1))  # Output: 4

n2 = 5
roads2 = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
print(solution.maximalNetworkRank(n2, roads2))  # Output: 5

n3 = 8
roads3 = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(solution.maximalNetworkRank(n3, roads3))  # Output: 5
