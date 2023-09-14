from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph represented as a dictionary where keys are source airports
        # and values are lists of target airports in lexical order.
        graph = {}
        for ticket in tickets:
            source, target = ticket
            if source in graph:
                graph[source].append(target)
            else:
                graph[source] = [target]

        # Sort the target airports lexicographically for each source airport.
        for source in graph:
            graph[source].sort()

        # Initialize an empty list to store the final itinerary.
        itinerary = []

        def dfs(node):
            # Visit all the neighbors of the current node.
            while node in graph and graph[node]:
                neighbor = graph[node].pop(0)  # Get the first neighbor.
                dfs(neighbor)  # Recursively visit the neighbor.
            itinerary.append(node)  # Add the current node to the itinerary.

        # Start the DFS from the "JFK" airport.
        dfs("JFK")

        # Reverse the itinerary to get the correct order.
        return itinerary[::-1]
    
s = Solution()

# Testcase 1:
print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Testcase 2:
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

# Testcase 3:
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# Output: ["JFK","NRT","JFK","KUL"]