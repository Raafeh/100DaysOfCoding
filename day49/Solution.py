import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character in the string
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Create a max heap to store characters based on their frequency
        max_heap = []
        for char, count in char_count.items():
            heapq.heappush(max_heap, (-count, char))
        
        result = []
        
        while len(max_heap) >= 2:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)
            
            # Append the characters to the result
            result.extend([char1, char2])
            
            # Decrement the counts and add back to heap if count is still greater than 0
            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))
        
        # If there's still a character left in the heap, append it to the result
        if max_heap:
            count, char = heapq.heappop(max_heap)
            if count < -1:
                return ""
            result.append(char)
        
        return ''.join(result)
s=Solution()

# Testcase 1:
print(s.reorganizeString("aab")) # "aba"

# Testcase 2:
print(s.reorganizeString("aaab")) # ""

# Testcase 3:
print(s.reorganizeString("vvvlo")) # "vlvov"