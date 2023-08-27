class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        tCount = 0  
        fCount = 0  
        maxCount = 0  
        left = 0  
        right = 0  
        
        while right < n:
            if answerKey[right] == 'T':
                tCount += 1
            else:
                fCount += 1
            
            # Check if the maximum count can be increased
            if max(tCount, fCount) + k >= right - left + 1:
                maxCount = max(maxCount, right - left + 1)
            else:
                # Move both pointers to the right
                if answerKey[left] == 'T':
                    tCount -= 1
                else:
                    fCount -= 1
                left += 1
            right += 1
        
        return maxCount

s=Solution()

# Test Case:1
print(s.maxConsecutiveAnswers("TTFF",2)) # Solution= 4

# Test Case:2
print(s.maxConsecutiveAnswers("TFFT",1)) # Solution= 3

# Test Case:3
print(s.maxConsecutiveAnswers("TTFTTFTT",1)) # Solution= 5