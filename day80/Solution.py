from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort the words by length so that we process shorter words before longer ones
        words.sort(key=len)
        
        # Initialize a dictionary to store the maximum chain length for each word
        max_chain_length = {}
        
        # Initialize the result to 1 since the minimum chain length is 1 for each word
        result = 1
        
        # Iterate through the sorted words
        for word in words:
            # Initialize the chain length for the current word to 1
            max_chain_length[word] = 1
            
            # Generate all possible predecessor words by removing one character at a time
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                
                # If the predecessor exists in max_chain_length and has a longer chain length,
                # update the chain length for the current word
                if predecessor in max_chain_length:
                    max_chain_length[word] = max(max_chain_length[word], max_chain_length[predecessor] + 1)
            
            # Update the overall result with the maximum chain length for the current word
            result = max(result, max_chain_length[word])
        
        return result
    
S = Solution()

# Testcase 1:
print(S.longestStrChain(["a","b","ba","bca","bda","bdca"])) # 4

# Testcase 2:
print(S.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])) # 5

# Testcase 3:
print(S.longestStrChain(["abcd","dbqca"])) # 1
