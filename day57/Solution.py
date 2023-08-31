from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []  # Create a list of intervals
        
        # Convert the tap ranges into interval format (start, end)
        for i in range(len(ranges)):
            intervals.append((max(0, i - ranges[i]), min(n, i + ranges[i])))
        
        intervals.sort()  # Sort the intervals based on their starting point
        end = 0  # Initialize the end point of the current interval
        farthest = 0  # Initialize the farthest point reachable
        
        taps_used = 0  # Count of taps used
        
        # Iterate through intervals to find the minimum number of taps needed
        for i in range(len(intervals)):
            start, new_end = intervals[i]
            
            if start > end:
                return -1  # There is a gap that cannot be covered
                
            if start > farthest:
                taps_used += 1
                farthest = end
                
            end = max(end, new_end)
            
            if end >= n:
                return taps_used + 1
                
        return -1  # Garden cannot be watered completely
    
s=Solution()

# Testcase 1:
print(s.minTaps(5, [3,4,1,1,0,0])) # Output = 1

# Testcase 2:
print(s.minTaps(3, [0,0,0,0])) # Output = -1

# Testcase 3:
print(s.minTaps(7, [1,2,1,0,2,1,0,1])) # Output = 3