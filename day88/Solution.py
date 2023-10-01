class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words
        words = s.split()
        
        # Reverse each word in the list
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words back together
        reversed_sentence = ' '.join(reversed_words)
        
        return reversed_sentence

s = Solution()

# Testcase 1:
print(s.reverseWords("Let's take LeetCode contest")) # Output: "s'teL ekat edoCteeL tsetnoc"

# Testcase 2:
print(s.reverseWords("God Ding")) # Output: "doG gniD"

# Testcase 3:
print(s.reverseWords("Hello World")) # Output: "olleH dlroW"