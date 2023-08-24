from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                result.append(self.format_line(line, maxWidth, line_length))
                line = [word]
                line_length = len(word)

        result.append(" ".join(line).ljust(maxWidth))
        return result

    def format_line(self, line, maxWidth, line_length):
        if len(line) == 1:
            return line[0].ljust(maxWidth)

        total_spaces = maxWidth - line_length
        space_gaps = len(line) - 1
        regular_space = total_spaces // space_gaps
        extra_space = total_spaces % space_gaps

        formatted_line = ""
        for i in range(len(line) - 1):
            formatted_line += line[i]
            formatted_line += ' ' * regular_space
            if extra_space > 0:
                formatted_line += ' '
                extra_space -= 1

        formatted_line += line[-1]
        return formatted_line

s=Solution()

# Testcase 1:
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

# Testcase 2:
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))

