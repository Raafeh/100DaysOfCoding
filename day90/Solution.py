from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = {}  
        good_pairs = 0  

        # Iterate through the array and count the occurrences of each number
        for num in nums:
            if num in count_dict:
                # If the number already exists in the dictionary, increment the count
                count_dict[num] += 1
            else:
                # If the number is not in the dictionary, add it with a count of 1
                count_dict[num] = 1
        
        # Iterate through the count_dict and calculate the number of good pairs for each number
        for count in count_dict.values():
            good_pairs += (count * (count - 1)) // 2
        
        return good_pairs

s = Solution()

# Testcase 1:
print(s.numIdenticalPairs([1,2,3,1,1,3])) # Output = 4

# Testcase 2:
print(s.numIdenticalPairs([1,1,1,1])) # Output = 6

# Testcase 3:
print(s.numIdenticalPairs([1,2,3])) # Output = 0