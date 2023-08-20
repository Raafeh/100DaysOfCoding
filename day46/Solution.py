import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts={}
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        s = paragraph.split()
        
        for word in s:
            if word not in banned or '':
                counts[word]=counts.get(word,0)+1
        bigcount = None
        bigword = None
        for word,count in counts.items():
            if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count
        
        return bigword
    
s=Solution()

# Testcase 1:
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
# Output: "ball"

# Testcase 2:
print(s.mostCommonWord("Hello how are doing",["hello"]))
# Output: "how"


